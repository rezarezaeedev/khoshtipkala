from django import forms
from django.core import validators


class  ContactForm(forms.Form):
    fullname=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام و نام خانوادگی','class':'form-control'}
        ),
        label='',
        validators=[validators.MaxLengthValidator(150,'نام و نام خانوادگی شما نمیتواند بیشتر از 150 حرف باشد')]
    )

    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'ایمیل','class':'form-control'}
        ),
        label='',
        validators=[validators.MaxLengthValidator(100,'ایمیل شما نمیتواند بیشتر از 150 حرف باشد')]
    )

    subject=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'عنوان','class':'form-control'}
        ),
        label='',
        validators=[validators.MaxLengthValidator(200,'عنوان پیام شما نمیتواند بیشتر از 150 حرف باشد')]
    )

    text=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'پیام خود را بنویسید...','class':'form-control','rows':'8' ,'id':'message','name':'message','required':''}
        ),
        label='',
        validators=[validators.MaxLengthValidator(600,'متن پیام شما نمیتواند بیشتر از 600 حرف باشد')]
    )













