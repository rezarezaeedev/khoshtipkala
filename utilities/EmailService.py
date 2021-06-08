from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import re

class EmailService:

    @staticmethod
    def _send_email(subject, from_email, to, template_name, context):
        html_message = render_to_string(template_name, context)

        plain_message = strip_tags(html_message)

        send_mail(subject=subject,
                  message=plain_message,
                  from_email=from_email,
                  recipient_list=to,
                  html_message=html_message
                  )

    @staticmethod
    def email_checker(email):
        email_result = re.match(r'^([0-9a-z])[0-9a-z_.-]{2,40}([0-9a-z])(@gmail\.com)$', email, flags=re.I | re.M)
        return bool(email_result)