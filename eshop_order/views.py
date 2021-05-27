from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from eshop_order.forms import OrderForm
from eshop_order.models import Order, OrderDetail
from eshop_products.models import Product


def add_user_order(request):
    orderlistform=OrderForm(request.POST or None)
    user=request.user
    if orderlistform.is_valid():
        product_id  =   orderlistform.cleaned_data.get('product_id')
        product     =   Product.objects.filter(id=product_id).first()
        count       =  orderlistform.cleaned_data.get('count')
        if user.is_authenticated:
            if count<1:
                count=1

            order=Order.objects.filter(owner=user,is_paid=False).last()  # get/create orderlist
            if order is None:
                order=Order.objects.create(owner=user,is_paid=False)

            orderdetail=OrderDetail.objects.filter(order=order,product=product).last()  # check exist product in orderlist for add/create
            if orderdetail is None:
                orderdetail=OrderDetail.objects.create(order=order,product=product, count=count,price=product.price)
            else:
                orderdetail.count+=count
                orderdetail.save()
            return redirect(reverse('productdetail',args=[product.objid,product.title]))
        return redirect(reverse('login')) # if not authenticated user
    return render(request, '404_error.html')


# # @login_required
# def add_user_order(request):
#     new_order_form=OrderDetailForm(request.POST or None )
#
#     if new_order_form.is_valid() and request.user.is_authenticated:
#         order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
#         if order is None:
#             order = Order.objects.create(owner_id =request.user.id, is_paid=False)
#
#         product_id = new_order_form.cleaned_data.get('product_id')
#         product = Product.objects.get(id=product_id)
#         count = new_order_form.cleaned_data.get('count')
#         if count <= 0:
#             count = 1
#         if order.orderdetail_set.filter(product_id=product.id).count() == 0:
#             order.orderdetail_set.create(order=order, product_id=product.id, price=product.price, count=count)
#         else:
#             updateorder=order.orderdetail_set.filter(product_id=product.id).first()
#             updateorder.count+=1
#             updateorder.save()
#         return redirect(reverse('productdetail',kwargs={ 'objid':product.objid,'title':product.title.replace(' ','-')}))
#
#     return redirect(reverse('login'))
