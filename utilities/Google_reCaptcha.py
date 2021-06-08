"""
Guide:
1-pip install django-recaptcha
2-put "captcha" in settings.INSTALLED_APPS
3-make reCaptcha_project for this django_project
4-change public_key & private_key to self reCaptcha_project
5-import & inherit template form of wich one these class's
* https://pypi.org/project/django-recaptcha/
* https://www.google.com/recaptcha/about/
"""

from django import forms
from captcha.fields import ReCaptchaField,ReCaptchaV3, ReCaptchaV2Checkbox

class reCaptchaV2(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            api_params={
                'hl':'fa'
            }),
        label='تصویر امنیتی',
        error_messages={
            'required':'خطای کپچا!!'
        },
    public_key = '6LcC4RsbAAAAAOceFxxSkTv3wZUUTbaOL2DHuhR0',  # for v2-checkbox
    private_key = '6LcC4RsbAAAAACqcMNRey6slZ3Ufythcmh385B_Z',  # for v2-checkbox

    )

# make reCaptcha_project for this django_project
class reCaptchaV3Form(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            api_params={
                'hl':'fa'
            }),
        label='تصویر امنیتی',
        error_messages={
            'required':'خطای کپچا!!'
        },
    public_key = '6Ld79hsbAAAAAFdEf3jcoA-IwD8saX_9mbl8bC1_',  # for v2-checkbox
    private_key = '6Ld79hsbAAAAAEm-SUswcwYvlt30lYRxKK4UjwCu',  # for v2-checkbox

    )
