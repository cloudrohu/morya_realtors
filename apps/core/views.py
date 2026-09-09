from django.shortcuts import render,redirect

from apps.core.models.website import Setting

def get_settings():
    """Helper function to fetch settings object safely"""
    return Setting.objects.first()


def about(request):
    return render(request, 'home/about.html', {'settings_obj': get_settings()})

def developers(request):
    return render(request, 'home/developers.html', {'settings_obj': get_settings()})

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
    return render(request, 'home/thank_you.html', {'settings_obj': get_settings()})



