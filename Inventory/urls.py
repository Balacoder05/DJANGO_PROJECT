from django.urls import path
from .views import *


urlpatterns=[
    path('home/',HomePage),
    path('about/',aboutpage),
    path('contact/',contactpage),
    path('services/',servicespage),
    path('products/add/',productsAdd),
    path('products/',AllProducts),
    path('products/delete/<int:id>/',DeleteProducts,name='product_delete'),
    path('products/update/<int:id>/',Product_Update,name='product_update'),

]