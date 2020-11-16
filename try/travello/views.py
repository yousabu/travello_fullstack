from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {"dest":dest})




def about(request):
    return render(request , 'about.html')   




def contact(request):
    return render(request, 'contact.html')    