from django.shortcuts import render
from .forms import*
from .models import*

# Create your views here.

def HomePage(request):
    context={
        "name":"Balamurugan",
        "role":"manager",
        "numbers":[1,2,3,4,5], 
        "marks":{
            "Tamil":100,
            "English":100,
        }
    }
    return render(request,'home.html',context)
 
def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")

def servicespage(request):
    
    return render(request,"services.html")

def productsAdd(request):

    context={
        'product_form':Product_Form()
    }

    if request.method == "POST":
        print(request.POST)

    return render(request,"products_add.html",context)