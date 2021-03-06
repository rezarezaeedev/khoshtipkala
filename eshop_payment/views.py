from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from zeep import Client
from eshop_order.models import Order
from eshop_payment.models import PaymentGateway

# MERCHANT = ''
# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09301162905'  # Optional
# CallbackURL = 'http://localhost:8000/payment/verify/' # Important: need to edit for realy server.

def get_currnet_time():
    current_time = datetime.now()
    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return date_time

@login_required(login_url='/login')
def send_payment_request(request,*args,**kwargs):
    paymentgateway=PaymentGateway.objects.filter(active=True).last()
    server=paymentgateway.server
    server=server+'/' if server[-1] != '/' else server
    CallbackURL=server+paymentgateway.callBackUrl
    client=Client(paymentgateway.clientURL)
    MERCHANT=paymentgateway.merchantID
    startpayURL=paymentgateway.startPayURL
    startpayURL = startpayURL + '/' if startpayURL[-1] != '/' else startpayURL
    total_amount=0
    user=request.user
    orderid=kwargs.get('orderid')
    openorder:Order=Order.objects.filter(owner=user,is_paid=False).last()
    if openorder is not None and openorder.orderdetail_set.all().count()!=0 :
        total_amount=openorder.get_total_price()[0]
        result = client.service.PaymentRequest(MERCHANT, total_amount, description, email, mobile, f'{CallbackURL}{openorder.id}')
        if result.Status == 100:
            return redirect(startpayURL + str(result.Authority))
        else:
            # return HttpResponse('Error code: ' + str(result.Status))
            return redirect('404-error')


def verify_payment(request, *args, **kwargs):
    paymentgateway=PaymentGateway.objects.filter(active=True).last()
    client = Client(paymentgateway.clientURL)
    MERCHANT=paymentgateway.merchantID
    user = request.user
    order_id=kwargs.get('order_id')
    openorder = Order.objects.filter (owner=user, is_paid=False, id=order_id).last()
    if request.GET.get('Status') == 'OK' and openorder is not None:
        amount = openorder.get_total_price_with_taxation()
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            # openorder =Order.objects.filter(owner=user,is_paid=False,id=order_id).last()
            # openorder =Order.objects.filter(id=order_id).last()
            # openorder =Order.objects.filter(owner=user,is_paid=False,id=order_id).last()
            openorder.is_paid=True
            openorder.payment_date = get_currnet_time()
            openorder.ref_id = str(result.RefID)
            openorder.save()
            # return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
            return render(request, 'payment_response.html', context={'data': 'پرداخت با موفقیت انجام شد', 'bolddata': ' تبریک ','refid':str(result.RefID)})
        elif result.Status == 101:
            # return HttpResponse('Transaction submitted : ' + str(result.Status))
            return render(request, 'payment_response.html', context={'data': 'این پرداخت قبلا انجام شده است', 'bolddata': ' توجه: ','refid':str(result.RefID)})
        else:
            # return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
            return render(request, 'payment_response.html', context={'data': 'پرداخت با خطا مواجه شده است!', 'bolddata': ' خطا: ','refid':str(result.RefID)})
    else:
        # return HttpResponse('Transaction failed or canceled by user')
        return render(request, 'payment_response.html', context={'data': 'پرداخت توسط کاربر لغو شده است!', 'bolddata': ' پشیمانی: '})


    # ############################## 4 Test #############################
    # print('پرداخت تستی')
    # openorder =Order.objects.filter(owner=user).last()
    # openorder.is_paid=False if openorder.is_paid else True
    # openorder.payment_date = get_currnet_time()
    # openorder.ref_id = '' if openorder.ref_id else '11111'
    # openorder.save()
    # return HttpResponse(
    #     f"""
    #    <h1 style='color:red'> پرداخت شد </h1>
    #    order_id :{order_id}<br>
    #    openorder :{openorder}<br>
    #    is_paid :{openorder.is_paid}<br>
    #    ref_id :{openorder.ref_id}<br>
    #    payment_date :{openorder.payment_date}<br>
    #       """
    # )
    # ############################## 4 Test #############################


def test(request):
    context={'data':'متن تست برای امتحان صفحه نمایش پاسخ درگاه پرداخت','bolddata':' توجه: ','refid':'000098435325 '}
    return render(request, 'payment_response.html', context)







































