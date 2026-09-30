from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project

def project_list_view(request):
    status = request.GET.get('status', '')
    projects_qs = Project.objects.all()

    if status:
        projects_qs = projects_qs.filter(status=status)

    paginator = Paginator(projects_qs, 6)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {
        'projects': projects,
        'selected_status': status,
        'status_choices': Project.STATUS_CHOICES,
        'page_title': "Nos Projets d'Impact - Pissy Vibes",
    }
    return render(request, 'projects/project_list.html', context)

def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    other_projects = Project.objects.exclude(id=project.id)[:3]
    context = {
        'project': project,
        'other_projects': other_projects,
        'page_title': f"{project.title} - Projets Pissy Vibes",
    }
    return render(request, 'projects/project_detail.html', context)
