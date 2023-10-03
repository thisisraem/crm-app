from django.shortcuts import render, redirect
from .models import Malls, Brands, CustomerRecords
from django.http import JsonResponse
from django.utils.translation import activate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def language(request):
    return render (request, 'language.html')

def success_submit(request):
    return render(request, 'success-submit.html')

def languageAz(request):
    activate('az')
    return render(request, 'language.html')

def home(request):
    malls = Malls.objects.all()
    brands = Brands.objects.all()
    context = {
        'title':'NOVCO CRM AZE',
        'malls': malls,
        'brands': brands
    }
    return render(request, 'index.html', context)

def get_brands(request):
    mall_id = request.GET.get('mall_id')
    brands = Brands.objects.filter(malls__id=mall_id).values('id', 'name')
    return JsonResponse({'brands': list(brands)})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        mobile_number = request.POST.get('operator-code') + request.POST.get('mobile-number')
        malls = request.POST.getlist('location')
        brands = request.POST.getlist('store')  # Get the selected brands from the form
        comments = request.POST.get('comments')

        customer = CustomerRecords(
            name=name,
            surname=surname,
            gender=gender,
            age=age,
            email=email,
            mobile_number=mobile_number,
            comments=comments
        )
        customer.save()

        malls = Malls.objects.filter(id__in=malls)
        customer.malls.set(malls)

        brands = Brands.objects.filter(id__in=brands)  # Filter the selected brands
        customer.brands.set(brands)  # Set the selected brands for the customer
        
        send_mail(
            '(Your title is here)',
            '(Your message is here)',
            settings.DEFAULT_FROM_EMAIL,  # Sender's email address
            [email],  # List of recipient email addresses
            fail_silently=False  # Set to True to suppress exceptions if any
        )
        

        # Display a success message
        messages.success(request, 'Thank you for submitting the form!')
        return redirect(success_submit)

    malls = Malls.objects.all()
    brands = Brands.objects.all()
    context = {
        'title': 'NOVCO CRM AZE',
        'malls': malls,
        'brands': brands
    }
    return render(request, 'language.html', context)


# def handling_404(request, exception):
#     return render (request, '404.html', {})
