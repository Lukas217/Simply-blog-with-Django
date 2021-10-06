
from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.views import View

def about_us(request):
    title="About us"
    context = {
        'title': title
    }
    return render(request, 'common/about.html', context)

def contact_view(request):
    title="Contact"
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')    
        data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,   
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['name'], message, '', ['lukiospl@gmail.com'])
    return render(request, 'common/contact.html', {'title': title})








