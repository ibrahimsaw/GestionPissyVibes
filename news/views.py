from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Category

def article_list_view(request):
    category_slug = request.GET.get('category', '')
    query = request.GET.get('q', '')

    articles_qs = Article.objects.filter(is_published=True).select_related('category', 'author')

    if category_slug:
        articles_qs = articles_qs.filter(category__slug=category_slug)
    if query:
        articles_qs = articles_qs.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(content__icontains=query)
        )

    categories = Category.objects.all()
    recent_articles = Article.objects.filter(is_published=True)[:4]

    paginator = Paginator(articles_qs, 6)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    context = {
        'articles': articles,
        'categories': categories,
        'selected_category': category_slug,
        'search_query': query,
        'recent_articles': recent_articles,
        'page_title': "Actualités & Blog - Pissy Vibes",
    }
    return render(request, 'news/article_list.html', context)

def article_detail_view(request, slug):
    article = get_object_or_404(Article.objects.select_related('category', 'author'), slug=slug, is_published=True)
    
    # Increment views
    Article.objects.filter(id=article.id).update(views_count=article.views_count + 1)
    
    related_articles = Article.objects.filter(is_published=True, category=article.category).exclude(id=article.id)[:3]
    recent_articles = Article.objects.filter(is_published=True).exclude(id=article.id)[:4]

    context = {
        'article': article,
        'related_articles': related_articles,
        'recent_articles': recent_articles,
        'page_title': f"{article.title} - Pissy Vibes",
    }
    return render(request, 'news/article_detail.html', context)
