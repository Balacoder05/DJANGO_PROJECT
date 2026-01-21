from django.shortcuts import render, redirect
from .models import Customer
from .forms import Customer_Form

# List all customers
def Allcustomers(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return render(request, 'customers.html', context)




def Addcustomers(request):
    context = {
        'customer_form': Customer_Form()
    }

    if request.method == "POST":
        customer_form = Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/order/customers/')  # redirect to all customers page

    return render(request, "customers_add.html", context)






def Delete_Customer(request,id):

    selected_customer=Customer.objects.get(id=id)
    selected_customer.delete()

    return redirect('/order/customers/')


def Customer_Update(request,id):

    selected_customer=Customer.objects.get(id=id)

    context={
        "customer_form" : Customer_Form(instance=selected_customer)

    }
    if request.method == 'POST':

        customer_form = Customer_Form(request.POST,instance=selected_customer)

        if customer_form.is_valid():

            customer_form.save()

            return redirect('/order/customers/')

    return render(request,'customers_add.html',context)


