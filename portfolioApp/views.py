from django.shortcuts import render
from portfolioApp.models import Contact,Pricing,Skills,Profile,ProfessionalExperience,WorkSummary
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

import requests

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def home(request):
    all_pricing = Pricing.objects.all()
    skills=Skills.objects.all()
    data=Profile.objects.all()
    bio_data=data[0]
    experiences=ProfessionalExperience.objects.all()
    work_summery=WorkSummary.objects.all()
    #products = Product.objects.all()
    product_details = []

    for experience in experiences:
        all_points = experience.exp_point.all()
        product_detail = {
            'experiences':experiences,
            'company': experience.company,
            'designation':experience.designation,
            'start_date':experience.start_date,
            'end_date':experience.end_date,
            'address':experience.address,

            'technology':experience.technology,

            'points': [point.summary.details for point in all_points],
        }

        product_details.append(product_detail)
    combined_data = [{'object': obj, 'product_name': name} for obj, name in zip(experiences, product_details)]

    #context = {'combined_data': combined_data}
    context = {'all_pricing':all_pricing,'skills':skills,'bio_data':bio_data,'experiences':experiences,'work_summery':work_summery,'combined_data':combined_data}
    return render(request, 'base.html', context)

def contactUs(request):
    print("######################################")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact.objects.create(name=name,email=email,subject=subject,message=message)

        contact.save()
        print("finally saved ######################################")
        email_subject = f'New contact {email}: {subject}'
        #email_message = note
        email_message = f'Name : {name}\n Subject : {subject}\n Message : {message}'

        #recipient_list = settings.EMAIL_HOST_USER
        #from_email = email

        #recipient_list = settings.EMAIL_HOST
        print("print  from inside form method #############******************#######################")
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

        #send_mail(email_subject, email_message, from_email, recipient_list)
        #return redirect("portfolioApp:home")
        return HttpResponseRedirect(reverse('portfolioApp:contact'))
    #context = {'form': form}
    #return render(request, 'contact/contact.html', context)
    return render(request, 'base.html')

#def pricing(request, pk):
#    all_pricing = Pricing.objects.all()
#    context = {'all_pricing':all_pricing}
#    return render(request, 'base.html', context)

