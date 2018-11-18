from django.shortcuts import render
from django.template import RequestContext

from emailconfirmation.models import EmailConfirmation


def confirm_email(request, confirmation_key):
    email_address = EmailConfirmation.objects.confirm_email(confirmation_key.lower())

    return render(
        request,
        "emailconfirmation/confirm_email.html", {
            "email_address": email_address,
        })
