from django.urls import path
from .views import *


urlpatterns=[
    path('home/',HomePage),
    path('about/',aboutpage),
    path('contact/',contactpage),
    path('services/',servicespage),

]