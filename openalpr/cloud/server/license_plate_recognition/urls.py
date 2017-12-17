from django.urls import path
from license_plate_recognition import views

urlpatterns = [
    path('licenseimages/', views.licence_imgs_list)
]
