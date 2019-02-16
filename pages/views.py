from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm
from .models import Main, Service, Career, AboutUs, Banner1, Banner2, WhatWeDo, JobAd, Carousel, Apply


from django.http import HttpResponseRedirect
# from .forms import UploadFileForm
from django.core.files.uploadedfile import SimpleUploadedFile
import mimetypes
from django.core.mail import EmailMultiAlternatives




# Create your views here.

#Home
def home(request):
    main = Main.objects.get(section = 'main')
    services = Service.objects.all()
    banner_1 = Banner1.objects.get(section = 'Banner 1')
    careers = Career.objects.get(section = 'Careers')
    banner_2 = Banner2.objects.get(section = 'Banner 2')
    about_us = AboutUs.objects.get(section = 'About Us')
    carousel = Carousel.objects.get(section = 'Carousel')
    what_we_do = WhatWeDo.objects.get(section = 'What We Do')

    context = {
    'main': main,
    'banner_1':banner_1,
    'services': services,
    'banner_2':banner_2,
    'careers': careers,
    'about_us': about_us,
    'carousel': carousel,
    'what_we_do': what_we_do,
    }

    return render(request, 'pages/home.html', context)



#What We Do
def what_we_do(request):
    what_we_do = WhatWeDo.objects.get(section = 'What We Do')
    services = Service.objects.all()
    main = Main.objects.get(section = 'main')
    careers = Career.objects.get(section = 'Careers')
    carousel = Carousel.objects.get(section = 'Carousel')




    context = {
    'what_we_do': what_we_do,
    'services': services,
    'main': main,
    'careers': careers,
    'carousel': carousel,
    }

    return render(request, 'pages/what_we_do.html', context)



#Careers
def careers(request):
    careers = Career.objects.get(section = 'Careers')
    about_us = AboutUs.objects.get(section = 'About Us')
    main = Main.objects.get(section = 'main')
    job_ad = JobAd.objects.get(section = 'Job Ad')
    carousel = Carousel.objects.get(section = 'Carousel')
    what_we_do = WhatWeDo.objects.get(section = 'What We Do')
    apply_objects = Apply.objects.all()


    context = {
    'careers': careers,
    'about_us': about_us,
    'main': main,
    'job_ad': job_ad,
    'what_we_do': what_we_do,
    'carousel': carousel,
    'apply_objects': apply_objects,
    }

    return render(request, 'pages/careers.html', context)




def apply(request, apply_id):
    apply = get_object_or_404(Apply, pk=apply_id)




    careers = Career.objects.get(section = 'Careers')
    about_us = AboutUs.objects.get(section = 'About Us')
    main = Main.objects.get(section = 'main')
    job_ad = JobAd.objects.get(section = 'Job Ad')
    carousel = Carousel.objects.get(section = 'Carousel')
    what_we_do = WhatWeDo.objects.get(section = 'What We Do')




    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        file = request.FILES['document']


        from_email = settings.EMAIL_HOST_USER

        to_email = apply.receiving_email

        email = EmailMultiAlternatives(
        request.POST.get('full_name') ,
        'phone ' + request.POST.get('phone') + ' email ' + request.POST.get('user_email'),
        from_email,
        [to_email]
        )
        email.attach(file.name, file.file.getvalue(), mimetypes.guess_type(file.name)[0])
        email.send()


    else:
        form = ContactForm()

    context = {
    'careers': careers,
    'about_us': about_us,
    'main': main,
    'job_ad': job_ad,
    'what_we_do': what_we_do,
    'carousel': carousel,
    'apply': apply,
    'form': form,

    }


    return render(request, 'pages/apply.html', context)
