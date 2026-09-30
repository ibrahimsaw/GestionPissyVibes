from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Action

def action_list_view(request):
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')
    query = request.GET.get('q', '')

    actions_qs = Action.objects.all()

    if category:
        actions_qs = actions_qs.filter(category=category)
    if status:
        actions_qs = actions_qs.filter(status=status)
    if query:
        actions_qs = actions_qs.filter(title__icontains=query) | actions_qs.filter(description__icontains=query)

    paginator = Paginator(actions_qs, 9)
    page_number = request.GET.get('page')
    actions = paginator.get_page(page_number)

    context = {
        'actions': actions,
        'selected_category': category,
        'selected_status': status,
        'search_query': query,
        'category_choices': Action.CATEGORY_CHOICES,
        'status_choices': Action.STATUS_CHOICES,
        'page_title': "Nos Actions - Pissy Vibes",
    }
    return render(request, 'activities/action_list.html', context)

def action_detail_view(request, slug):
    action = get_object_or_404(Action, slug=slug)
    related_actions = Action.objects.filter(category=action.category).exclude(id=action.id)[:3]
    context = {
        'action': action,
        'related_actions': related_actions,
        'page_title': f"{action.title} - Actions Pissy Vibes",
    }
    return render(request, 'activities/action_detail.html', context)
