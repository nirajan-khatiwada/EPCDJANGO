from django.shortcuts import render
from .models import *
from .forms import ContactFormModelForm
from django.contrib import messages
from django.template.loader import render_to_string
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
def home(request):
    if request.method == "POST":
      
        
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            notices =[ data.email for data in EmailRecipient.objects.all()]
            notice_email = render_to_string('notice.html',{'name':form.cleaned_data['name'],'email':form.cleaned_data['email'],'phone':form.cleaned_data['phone'],'service':form.cleaned_data['service'],'message':form.cleaned_data['message'],'date':datetime.now()})
            email=EmailMultiAlternatives("Important : Your Order Has Been Confirmed","Order Confirmed","Notice <contact@withepc.com>",to=notices)
            email.attach_alternative(notice_email, "text/html")
            email.send()



            booking=render_to_string('booked.html',{'name':form.cleaned_data['name'],'email':form.cleaned_data['email'],'phone':form.cleaned_data['phone'],'service':form.cleaned_data['service']})
            email=EmailMultiAlternatives("Order Confirmed","Order Confirmed","Order <contact@withepc.com>",to=[form.cleaned_data['email']])
            email.attach_alternative(booking, "text/html")
            email.send()
        
            form.save()
            messages.success(request, "Your message has been sent successfully.check your email")
            form = ContactFormModelForm()  # Reset the form after saving
        else:
            messages.success(request, "Error! Please Enter Data Correctly.")


    else:

        form = ContactFormModelForm()
    
    

    contact_info = ContactInfo.objects.first()
    social_links = SocialMedia.objects.all()
    hero_slides = HeroSlide.objects.filter(is_active=True)
    ServiceHeaders = ServiceHeader.objects.first()
    services = Service.objects.filter(is_active=True)
    logo = Logo.objects.first()
    why_choose_header = WhyChooseHeader.objects.first()
    why_choose_features = WhyChooseFeature.objects.filter(is_active=True)
    about_us_header = AboutUsHeader.objects.first()
    about_counts = AboutCount.objects.filter(is_active=True)
    teams = TeamHeader.objects.first()
    team_members = TeamMember.objects.filter(is_active=True)
    contact_header = ContactHeader.objects.first()
    working_hours = WorkingHours.objects.first()
    colors = [
        'bg-gradient-to-tr from-green-500 to-teal-600',
        'bg-gradient-to-tr from-blue-500 to-indigo-600',
        'bg-gradient-to-tr from-purple-500 to-pink-600'
    ]
    if len(about_counts) > len(colors):
        colors = colors * (len(about_counts) // len(colors) + 1)
    about_counts_with_colors = zip(about_counts, colors)

    context = {
        'contact_info': contact_info,
        'social_links': social_links,
        'logo': logo,
        'hero_slides': hero_slides,
        'services': services,
        'ServiceHeader': ServiceHeaders,
        'why_choose_header': why_choose_header,
        'why_choose_features': why_choose_features,
        'about_us_header': about_us_header,
        'about_counts': about_counts_with_colors,
        'teams': teams,
        'team_members': team_members,
        'contact_header': contact_header,
        'working_hours': working_hours,
        'form': form
    }

    return render(request, "index.html", context)

