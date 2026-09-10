from django.shortcuts import render
from apps.core.models import Setting
from apps.properties.models import Project



def dashboard(request):

    settings_obj = Setting.objects.first()
    projects = Project.objects.filter(parent__isnull=True)[:9]
    
    return render(
        request,
        "home/index.html",
        {
            "settings_obj": settings_obj,
            "projects": projects,

        }
    )

