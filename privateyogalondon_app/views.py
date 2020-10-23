from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Homepage
    """
    return render(request, 'privateyogalondon_app/index.html')

def faq(request):
    """
    Homepage
    """
    return render(request, 'privateyogalondon_app/faq.html')

def privacypolicy(request):
    """
    Homepage
    """
    return render(request, 'privateyogalondon_app/privacypolicy.html')