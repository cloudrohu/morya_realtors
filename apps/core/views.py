from django.shortcuts import render,redirect

# Create your views here.

def about(request):
  
    return render(request, 'home/about.html',)


def developers(request):
  
    return render(request, 'home/developers.html',)    

def localities(request):
  
    return render(request, 'home/localities.html',)    

def FAQs(request):
  
    return render(request, 'home/faqs.html',)

