from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
# Create your views here.
def home(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customer = customers.count()

    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers, 
               'total_orders':total_order, 'delivered':delivered,
               'pending':pending }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products':products }
    return render(request, 'accounts/products.html', context)

def customer(request, pk_test):
    # GET CUSTOMER BY ID
    customer = Customer.objects.get(id = pk_test)
    #GET ALL ORDER FROM CUSTOMER ID
    orders = customer.order_set.all()
    #COUNT OF ORDERS
    order_count = orders.count()

    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
        OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
        customer = Customer.objects.get(id=pk)
        formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
        if request.method == 'POST':
            # form = OrderForm(request.POST)
            formset = OrderFormSet(request.POST, instance=customer)
            if formset.is_valid():
                formset.save()
                return redirect('/')

        context = {'form':formset}
        return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)