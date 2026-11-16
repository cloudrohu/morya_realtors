from django.shortcuts import render
from django.db.models import Count,Q
from apps.core.models import Setting , Why_Choose , FAQ
from apps.properties.models import Project
from apps.properties_utility.models import Bank
from apps.blog.models import Article


def dashboard(request):
    settings_obj = Setting.objects.first()
    projects = Project.objects.filter(parent__isnull=True)[:9]


    new_launch_projects = (
        Project.objects.filter(
            parent__isnull=True,
            construction_status="New Launch",
            property_type__name="Residential",
        )
        .prefetch_related("configurations")
        .select_related("locality", "developer")[:9]
    )

    possession_statuses = [
        {
            "title": "Ready to Move",
            "status": "Ready To Move",
            "image": settings_obj.ready_to_move if settings_obj and settings_obj.ready_to_move else None,
            "icon": "fas fa-key",
            "number": "01",
        },
        {
            "title": "Partially Ready to Move",
            "status": "Partially Ready To Move",
            "image": settings_obj.partially_ready_to_move if settings_obj and settings_obj.partially_ready_to_move else None,
            "icon": "fas fa-building",
            "number": "02",
        },
        {
            "title": "Under Construction",
            "status": "Under Construction",
            "image": settings_obj.under_construction if settings_obj and settings_obj.under_construction else None,
            "icon": "fas fa-hard-hat",
            "number": "03",
        },
        {
            "title": "New Launch",
            "status": "New Launch",
            "image": settings_obj.new_launch if settings_obj and settings_obj.new_launch else None,
            "icon": "fas fa-rocket",
            "number": "04",
        },
        {
            "title": "Upcoming Projects",
            "status": "Upcoming",
            "image": settings_obj.upcoming_projects if settings_obj and settings_obj.upcoming_projects else None,
            "icon": "fas fa-city",
            "number": "05",
        },
        {
            "title": "deleverd",
            "status": "deleverd",
            "image": settings_obj.deleverd if settings_obj and settings_obj.deleverd else None,
            "icon": "fas fa-check-circle",
            "number": "06",
        },
    ]

    for item in possession_statuses:
        item["project_count"] = Project.objects.filter(
            parent__isnull=True,
            construction_status=item["status"],
        ).count()

    why_choose = Why_Choose.objects.filter(setting=settings_obj).order_by("order")
    faqs = FAQ.objects.filter(setting=settings_obj)
    banks = Bank.objects.all()

    featured_article = Article.objects.filter(is_published=True).order_by('-created_at').first()

    # Fetch the next 3 published articles for the grid cards (exclude the featured one)
    grid_articles = Article.objects.filter(is_published=True).order_by('-created_at')
    if featured_article:
        grid_articles = grid_articles.exclude(id=featured_article.id)
    grid_articles = grid_articles[:3]

    top_localities = (
        Project.objects
        .filter(is_active=True, locality__isnull=False)
        .values(
            "locality", 
            "locality__name", 
            "locality__image",
            "locality__description",
        )
        .annotate(project_count=Count("id"))
        .order_by("-project_count", "locality__name")[:8]
    )

    return render(
        request,
        "home/index.html",
        {
            "settings_obj": settings_obj,
            "new_launch_projects": new_launch_projects,
            "why_choose": why_choose,
            "faqs": faqs,
            "banks": banks,
            "top_localities": top_localities,
            "projects": projects,
            "featured_article": featured_article,
            "possession_statuses": possession_statuses,
            "grid_articles": grid_articles,
        }
    )

