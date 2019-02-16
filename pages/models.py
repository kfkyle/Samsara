from django.db import models

# Create your models here.

icon_choices = (
('fas fa-laptop-code', 'Laptop'),
('fas fa-user', 'User'),
('fas fa-network-wired', 'Network'),
('fas fa-globe-america', 'Globe'),
('fas fa-layer-group', 'Layer'),
('fas fa-chart-pie', 'Pie Chart'),
('fas fa-chart-line', 'Line Chart'),
)




# Main
class Main(models.Model):
    section = models.CharField(max_length=80, editable=False, default='main')
    main_title = models.CharField(max_length=80)
    back_drop = models.ImageField(upload_to ='photos/%Y/%m/%d')


    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name_plural = "Main"







# Services
class Service(models.Model):

    title = models.CharField(max_length=80)
    icon = models.CharField(max_length=80, choices = icon_choices)
    display = models.ImageField(upload_to ='photos/%Y/%m/%d')
    sub_title = models.CharField(max_length=400, null=True)

    content_1 = models.CharField(max_length=400, null=True)
    content_2 = models.CharField(max_length=400, null=True)
    content_3 = models.CharField(max_length=400, null=True)

    img_1 = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True,)
    sub_header_1 = models.CharField(max_length=200, null=True, blank=True)
    img_text_1 = models.CharField(max_length=200, null=True, blank=True)

    img_2 = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True,)
    sub_header_2 = models.CharField(max_length=200, null=True, blank=True)
    img_text_2 = models.CharField(max_length=200, null=True, blank=True)

    img_3 = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True,)
    sub_header_3 = models.CharField(max_length=200, null=True, blank=True)
    img_text_3 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.sub_title[:100]

    class Meta:
        verbose_name_plural = "Service"



# Banner 1
class Banner1(models.Model):
    section = models.CharField(max_length=80, editable=False, default='Banner 1')
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Banner 1"



# Careers
class Career(models.Model):

    title = models.CharField(max_length=80, null=True)
    tag_line = models.CharField(max_length=80, null=True)
    section = models.CharField(max_length=80, editable=False, default='Careers')
    display = models.ImageField(upload_to ='photos/%Y/%m/%d')
    sub_title = models.CharField(max_length=400, null=True)

    content_1 = models.CharField(max_length=400, null=True)
    content_2 = models.CharField(max_length=400, null=True)
    content_3 = models.CharField(max_length=400, null=True)

    img_1 = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True,)
    sub_header_1 = models.CharField(max_length=200, null=True, blank=True)
    img_text_1 = models.CharField(max_length=200, null=True, blank=True)

    img_2 = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True,)
    sub_header_2 = models.CharField(max_length=200, null=True, blank=True)
    img_text_2 = models.CharField(max_length=200, null=True, blank=True)

    img_3 = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True,)
    sub_header_3 = models.CharField(max_length=200, null=True, blank=True)
    img_text_3 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Career"



# Banner2
class Banner2(models.Model):
    section = models.CharField(max_length=80, editable=False, default='Banner 2')
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Banner 2"



# About us
class AboutUs(models.Model):
    section = models.CharField(max_length=80, editable=False, default='About Us')
    title = models.CharField(max_length=80)
    display = models.ImageField(upload_to ='photos/%Y/%m/%d')

    sub_header_1 = models.CharField(max_length=200, null=True, blank=True)
    content_1 = models.TextField(blank=True)

    sub_header_2 = models.CharField(max_length=200, null=True, blank=True)
    content_2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"



#Why us main
class WhatWeDo(models.Model):
    section = models.CharField(max_length=80, editable=False, default='What We Do')
    main_title = models.CharField(max_length=80)
    tag_line = models.CharField(max_length=80, null=True)
    back_drop = models.ImageField(upload_to ='photos/%Y/%m/%d')
    side_display = models.ImageField(upload_to ='photos/%Y/%m/%d', null=True)


    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name_plural = "What We Do"



#Job Ad

class JobAd(models.Model):
    header = models.CharField(max_length=80, null=True)
    section = models.CharField(max_length=80, editable=False, default='Job Ad')
    title = models.CharField(max_length=80)
    ad = models.TextField()

    sub_header_1 = models.CharField(max_length=80, null=True)
    bullet_1 = models.CharField(max_length=80, null=True)
    bullet_2 = models.CharField(max_length=80, null=True)
    bullet_3 = models.CharField(max_length=80, null=True)
    bullet_4 = models.CharField(max_length=80, null=True)
    bullet_5 = models.CharField(max_length=80, null=True)

    sub_header_2 = models.CharField(max_length=80, null=True)
    second_bullet_1 = models.CharField(max_length=80, null=True)
    second_bullet_2 = models.CharField(max_length=80, null=True)
    second_bullet_3 = models.CharField(max_length=80, null=True)
    second_bullet_4 = models.CharField(max_length=80, null=True)
    second_bullet_5 = models.CharField(max_length=80, null=True)

    sub_header_3 = models.CharField(max_length=80, null=True)
    third_bullet_1 = models.CharField(max_length=80, null=True)
    third_bullet_2 = models.CharField(max_length=80, null=True)
    third_bullet_3 = models.CharField(max_length=80, null=True)

    apply = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.title



class Carousel(models.Model):
        section = models.CharField(max_length=80, editable=False, default='Carousel')

        header_1 = models.CharField(max_length=80, null=True)

        header_2 = models.CharField(max_length=80, null=True)

        header_3 = models.CharField(max_length=80, null=True)

        def __str__(self):
            return self.section



class Apply(models.Model):
    section = models.CharField(max_length=80, editable=False, default='Apply')
    city = models.CharField(max_length=80, null=True)
    receiving_email = models.CharField(max_length=80, null=True)


    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = "Apply"
