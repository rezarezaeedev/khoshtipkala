from django import forms
from django.core import validators

class OrderForm(forms.Form):
    product_id=forms.IntegerField(
        widget=forms.HiddenInput(
            attrs={}
        )
    )

    count=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={ }
        ),
        initial=1,
        validators=[validators.MinValueValidator(1,'حداقل تعداد انتخاب 1 میباشد!!'),
                    validators.MaxValueValidator(20,'حداکثر تعداد انتخاب 20 میباشد!!'),

                    ]
    )
