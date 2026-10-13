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

    why_choose = Why_Choose.objects.filter(setting=settings_obj).order_by("order")
    faqs = FAQ.objects.filter(setting=settings_obj)
    banks = Bank.objects.all()

    featured_article = Article.objects.filter(is_published=True).order_by('-created_at').first()

    # Fetch the next 3 published articles for the grid cards (exclude the featured one)
    grid_articles = Article.objects.filter(is_published=True).order_by('-created_at')
    if featured_article:
        grid_articles = grid_articles.exclude(id=featured_article.id)
    grid_articles = grid_articles[:3]

    status_counts = Project.objects.filter(parent__isnull=True).aggregate(
        new_launch=Count("id", filter=Q(construction_status="New Launch")),
        under_construction=Count("id", filter=Q(construction_status="Under Construction")),
        ready_to_move=Count("id", filter=Q(construction_status="Ready To Move")),
    )

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
            "status_counts": status_counts,
            "projects": projects,
            "featured_article": featured_article,
            "grid_articles": grid_articles,
        }
    )

