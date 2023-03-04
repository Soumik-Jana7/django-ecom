from django.shortcuts import render

from datetime import datetime
from hello.models import Contact

from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'prop1' : 'rendering prop1'
    }
    messages.success(request, 'Your details have been submitted')
    return render(request, 'index.html', context)
    #return HttpResponse('You are in index of hello app')

def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')


