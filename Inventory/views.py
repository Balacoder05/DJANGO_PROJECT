from django.shortcuts import render

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
    return render(request,'index.html',context)
 
