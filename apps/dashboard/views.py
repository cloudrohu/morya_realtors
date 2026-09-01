from django.shortcuts import render
from apps.core.models import Setting


def dashboard(request):

    settings_obj = Setting.objects.first()



    return render(
        request,
        "home/index.html",
        {
            "settings_obj": settings_obj,


        }
    )