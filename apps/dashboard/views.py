from django.shortcuts import render
from apps.core.models import Setting , Why_Choose , FAQ
from apps.properties.models import Project
from apps.properties_utility.models import Bank




def dashboard(request):

    settings_obj = Setting.objects.first()
    projects = Project.objects.filter(parent__isnull=True)[:9]
    new_launch_projects = Project.objects.filter(parent__isnull=True,construction_status="New Launch",property_type__name="Residential",)[:9]
    why_choose = Why_Choose.objects.filter(setting=settings_obj).order_by("order")
    faqs = FAQ.objects.filter(setting=settings_obj)

    banks = Bank.objects.all()


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
        }
    )       

