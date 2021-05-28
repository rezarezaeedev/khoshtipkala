from django import forms
from django.contrib.auth.validators import validators

from eshop_products.models import CommentProduct


class CommentForm(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام و نام خانوادگی'}
        ),
        label='',

        validators=[
            validators.MaxLengthValidator(302,'طول نامتان بیش از حد انتظار شده است'),
            validators.MinLengthValidator(3,'طول نامتان کمتر از 3 حرف شده است'),
        ]
    )

    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'پست الکترونیک'}
        ),
        label='',

    )

    rate=forms.CharField(
        widget=forms.Select(
            attrs={},choices=CommentProduct.Rate.choices
        ),
        label='آیا این محصول را دوست داشتید؟',
    )

    text=forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder':'متن پیام خود را وارد کنید...'}
        ),
        label='',

        validators=[
            validators.MaxLengthValidator(1000,'طول پیامتان بیش از حد 1000 حرف شده است'),
            validators.MinLengthValidator(4,'طول پیامتان کمتر از 4 حرف شده است'),
        ]
    )


class FavoriteForm(forms.Form):
    product_objid=forms.CharField(
        widget=forms.HiddenInput()
    )
