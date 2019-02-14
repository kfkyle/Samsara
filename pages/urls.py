
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('what_we_do/', views.what_we_do, name="what_we_do"),
    # path('apply/', views.apply, name="apply"),
    path('apply/<int:apply_id>', views.apply, name="apply"),
    path('careers/', views.careers, name="careers"),
]
