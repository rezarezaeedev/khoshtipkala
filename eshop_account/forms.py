from django import forms
from django.contrib.auth.models import User
from django.core import validators

from utilities.Google_reCaptcha import reCaptchaV2Form


class loginForm(reCaptchaV2Form,forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام کابری'}
        ),
    label='نام کاربری',
    )


    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'رمز عبور'}
        ),
    label='رمز عبور',
    )

    def clean_username(self):
        username=self.cleaned_data.get('username')
        is_username_exists = User.objects.filter(username=username).exists()
        if not is_username_exists:
            raise forms.ValidationError('نام کاربری وارد شده اشتباه میباشد')
        return username

class registerForm(reCaptchaV2Form,forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام کاربری خود را انتخاب کنید','maxlength':'20','minlength':'4'},
        ),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(20,'نام کاربری نمیتواند بیشتر از 20 کاراکتر باشد'),
            validators.MinLengthValidator(4,'نام کاربری نمیتواند کمتر از 4 کاراکتر باشد'),
            validators.RegexValidator('^[a-zA-Z0-9_]+[a-zA-Z0-9]$','فقط میتوانید از حروف بزرگ و کوچک لاتین, اعداد و آندرلاین استفاده کنید'),
            validators.RegexValidator('^[a-zA-Z]','کاراکتر اول باید از حروف بزرگ و کوچک لاتین باشد'),

        ],
        required=True,
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'پست الکترونیک خود را انتخاب کنید'},
        ),
        label='پست الکترونیک',
        validators=[
            validators.EmailValidator('لطفا پست الکترونیک خود را اصلاح کنید'),
            # validators.RegexValidator()
        ],
        required=True,
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'یک رمز عبور انتخاب کنید'},
        ),
        label='رمز عبور',
        validators=[

        ],
        required=True,
    )

    re_password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'رمز عبور خود را تکرار کنید'},
        ),
        label='تکرار رمز عبور',
        validators=[],
        required=True,
    )

    def clean_username(self):
        username=self.cleaned_data.get('username')
        is_exists_username = User.objects.filter(username=username).exists()
        if is_exists_username:
            raise forms.ValidationError('این نام کاربری گرفته شده است')
        return username

    def clean_re_password(self):
        password=self.cleaned_data.get('password')
        re_password=self.cleaned_data.get('re_password')
        if re_password!=password:
            raise forms.ValidationError('تکرار رمز عبور مطابقت ندارد!')
        return  re_password

    def clean_email(self):
        email=self.cleaned_data.get('email')
        is_exists_email=User.objects.filter(email=email)
        if is_exists_email:
            raise forms.ValidationError('این پست الکترونیک قبلا ثبت شده است.لطفا با آدرس دیگری امتحان کنید')
        return email

    def clean_password(self):
        password=self.cleaned_data.get('password')
        if len(password)<8 or len(password)>=20:
            raise forms.ValidationError('رمز عبور باید حداقل 8 کاراکتر و حداکثر 20 کاراکتر باشد')
        return password


class EditUserDataForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام کاربری جدید را انتخاب کنید','maxlength':'20','minlength':'2','class':'form-control'},
        ),
        label='نام کاربری',
        required=False,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام خود را انتخاب کنید','maxlength':'20','minlength':'2','class':'form-control '},
        ),
        label='نام',
        required=True,
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'نام خانوادگی را انتخاب کنید','maxlength':'20','minlength':'2','class':'form-control '},
        ),
        label='نام خانوادگی',
        required=True,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'پست الکترونیک خود را انتخاب کنید','class':'form-control'},
        ),
        label='پست الکترونیک',
        required=True,
    )

    def clean_username(self):
        username=self.cleaned_data.get('username').strip()
        if username == '':
            raise forms.ValidationError('نمیتواند خالی باشد')
        return username


    def clean_email(self):
        email=self.cleaned_data.get('email').strip()
        if email == '':
            raise forms.ValidationError('نمیتواند خالی باشد')
        return email