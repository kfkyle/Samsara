from django.contrib import admin
from .models import Main, WhyUs, Service, Career, AboutUs, Banner1, Banner2, WhatWeDo, JobAd, Carousel, Apply
from django.forms import TextInput, Textarea
from django.db import models



class BoxSize(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Service, BoxSize)
admin.site.register(Main, BoxSize)
admin.site.register(WhyUs, BoxSize)
admin.site.register(Career, BoxSize)
admin.site.register(AboutUs, BoxSize)
admin.site.register(Banner1, BoxSize)
admin.site.register(Banner2, BoxSize)
admin.site.register(WhatWeDo, BoxSize)
admin.site.register(JobAd, BoxSize)
admin.site.register(Carousel, BoxSize)
admin.site.register(Apply, BoxSize)
# Register your models here.
