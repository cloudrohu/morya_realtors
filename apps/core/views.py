from django.shortcuts import render,redirect
from django.db.models import Count

from apps.core.models.website import Setting , About , ImpactMetric, Milestone

from apps.properties.models import Developer


def get_settings():
    """Helper function to fetch settings object safely"""
    return Setting.objects.first()


def about(request):
    settings_obj = get_settings()
    about_obj = About.objects.filter(setting=settings_obj).first()


    impact_metrics = ImpactMetric.objects.filter(setting=settings_obj).order_by("order", "-created_at")

    milestones = Milestone.objects.filter(setting=settings_obj).order_by("year")


    return render(
        request,
        'home/about.html',
        {
            'settings_obj': settings_obj,
            'about_obj': about_obj,
            'impact_metrics': impact_metrics,
            'milestones': milestones,
        }
    )

def developers(request):

    developers = (
        Developer.objects
        .annotate(
            project_count=Count("projects", distinct=True)
        )
        .filter(
            project_count__gt=0
        )
        .order_by("-project_count")
    )

    return render(
        request,
        "home/developers.html",
        {
            "settings_obj": get_settings(),
            "developers": developers,
        }
    )

def localities(request):
    return render(request, 'home/localities.html', {'settings_obj': get_settings()})

def services(request):
    return render(request, 'home/services.html', {'settings_obj': get_settings()})

def FAQs(request):
    return render(request, 'home/faqs.html', {'settings_obj': get_settings()})

def Calculator(request):
    return render(request, 'home/calculator.html', {'settings_obj': get_settings()})

def Contact(request):
    return render(request, 'home/contact.html', {'settings_obj': get_settings()})

def Privacy_Policy(request):
    return render(request, 'home/privacy_policy.html', {'settings_obj': get_settings()})

def terms_of_service(request):
    return render(request, 'home/terms_of_service.html', {'settings_obj': get_settings()})

def disclaimer(request):
    return render(request, 'home/disclaimer.html', {'settings_obj': get_settings()})

def thank_you(request):
    return render(request, 'home/disclaimer.html', {'settings_obj': get_settings()})


def portfolio(request):
    return render(request, 'home/portfolio.html', {'settings_obj': get_settings()})


