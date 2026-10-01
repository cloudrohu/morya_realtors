from django.shortcuts import render
from django.db.models import Count
from apps.core.models import Setting , Why_Choose , FAQ
from apps.properties.models import Project
from apps.properties_utility.models import Bank





def dashboard(request):
    settings_obj = Setting.objects.first()
    projects = Project.objects.filter(parent__isnull=True)[:9]
    new_launch_projects = Project.objects.filter(
        parent__isnull=True,
        construction_status="New Launch",
        property_type__name="Residential",
    )[:9]
    why_choose = Why_Choose.objects.filter(setting=settings_obj).order_by("order")
    faqs = FAQ.objects.filter(setting=settings_obj)
    banks = Bank.objects.all()

    # Dynamic Top Localities fetch karein (Top 8 items)
    top_localities = (
        Project.objects
        .filter(is_active=True, locality__isnull=False)
        .values(
            "locality", 
            "locality__name", 
            "locality__image",
            "locality__description",  # Agar description model me ho
        )
        .annotate(project_count=Count("id"))
        .order_by("-project_count", "locality__name")[:8]
    )

    return render(
        request,
        "home/index.html",
        {
            "settings_obj": settings_obj,
            "projects": projects,
            "new_launch_projects": new_launch_projects,
            "why_choose": why_choose,
            "faqs": faqs,
            "banks": banks,
            "top_localities": top_localities,
        }
    )

