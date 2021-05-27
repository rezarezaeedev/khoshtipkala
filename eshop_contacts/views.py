from django.shortcuts import render

# Create your views here.
from eshop_contacts.forms import ContactForm
from eshop_contacts.models import ContactUs
from eshop_sitesetting.models import SiteSetting


def contact_us(request):
    contactform=ContactForm(request.POST or None)
    sitesetting=SiteSetting.objects.all().last()

    if contactform.is_valid():
        fullname=contactform.cleaned_data.get('fullname')
        email=contactform.cleaned_data.get('email')
        subject=contactform.cleaned_data.get('subject')
        text=contactform.cleaned_data.get('text')
        userobject=request.user
        ContactUs.objects.create(fullname=fullname,email=email,subject=subject,text=text,userobject=userobject)
        # todo : Your ticket was saved success
        contactform=ContactForm()

    context={
        'contactform':contactform,
        'sitesetting':sitesetting
    }
    return render(request, 'contacts/contact_us.html', context=context)

