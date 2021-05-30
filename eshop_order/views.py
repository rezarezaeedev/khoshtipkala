from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from eshop_order.forms import *
from eshop_order.models import Order, OrderDetail
from eshop_products.models import Product

@login_required(login_url='/login')
def add_user_order(request):
    orderlistform=OrderForm(request.POST or None)
    user=request.user
    if orderlistform.is_valid():
        product_objid   =   orderlistform.cleaned_data.get('product_objid')
        product         =   Product.objects.filter(objid=product_objid).first()
        count           =   orderlistform.cleaned_data.get('count')
        if product.beExist:
            order=Order.objects.filter(owner=user,is_paid=False).last()  # get/create orderlist
            if order is None:
                order=Order.objects.create(owner=user,is_paid=False)

            orderdetail=OrderDetail.objects.filter(order=order,product=product).last()  # check exist product in orderlist for add/create
            if orderdetail is None:
                orderdetail=OrderDetail.objects.create(order=order,product=product, count=count,price=product.price)
            else:
                orderdetail.count+=count
                orderdetail.save()
        return redirect(reverse('productdetail',args=[product.objid,product.title.replace(' ','-')]))
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

@login_required(login_url='/login')
def user_open_order_list(request):
    user=request.user
    context={
        'openorder':None,
        'detailorder':None,
    }

    openorder:Order=Order.objects.filter(owner=user, is_paid=False).last()
    if openorder is not None:
        detailorder = openorder.orderdetail_set.all()
        context['openorder']=openorder
        context['detailorder']=detailorder

    return render(request, 'order/user_open_order_list.html', context)

@login_required(login_url='/login')
def change_count_product_in_open_order(request,objid,mode):
    user=request.user
    order=Order.objects.filter(owner=user,is_paid=False).last()
    orderdetail=order.orderdetail_set.filter(product__objid=objid).last()
    try:
        mode=int(mode)
    except:
        return render(request,'404_error.html')

    if mode==1:
        if orderdetail.product.beExist:
            orderdetail.count+=1
            orderdetail.save()
    elif orderdetail.count<2 or mode==-1:
        orderdetail.delete()
    else:
        orderdetail.count-=1
        orderdetail.save()

    return redirect(reverse('user-open_order'))

