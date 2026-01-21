from django.urls import path
from .views import *

urlpatterns = [
        path('customers/', Allcustomers),
        path('customers/add/', Addcustomers),
        path('customers/delete/<int:id>/', Delete_Customer,name="customer_delete"),
        path('customers/update/<int:id>/', Customer_Update,name="customer_update"),

       

]
