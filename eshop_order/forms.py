from django import forms
from django.core import validators

from eshop_products.models import Product


class OrderForm(forms.Form):
    product_objid=forms.CharField(
        widget=forms.HiddenInput(
            attrs={}
        )
    )

    count=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'min':'1','max':'20'}
        ),
        initial=1,
        validators=[validators.MinValueValidator(1,'حداقل تعداد انتخاب 1 میباشد!!'),
                    validators.MaxValueValidator(20,'حداکثر تعداد انتخاب 20 میباشد!!'),
                    ]
    )

    def clean_product_objid(self):
        objid=self.cleaned_data.get('product_objid')
        if Product.objects.filter(objid=objid).last() is None:
            raise forms.ValidationError('خطا ناشناخته')
        return objid

    def clean_count(self):
        count=self.cleaned_data.get('count')
        if count<1 or (not type(count) is int):
            count=1
        return count

