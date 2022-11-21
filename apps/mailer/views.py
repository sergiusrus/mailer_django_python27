# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template import loader

from .models import Subscriber


def index(request):
    subscribers_list = Subscriber.objects.order_by('id').all()
    context = {'subscribers_list': subscribers_list}
    return render(request, 'mailer/index.html', context)


def sender(request):
    subscribers_list = Subscriber.objects.order_by('id').all()
    massages_sent = True
    mail_template = loader.get_template('mailer/mail_template.html')

    for subscriber in subscribers_list:
        context = {
            'user_name': subscriber.name,
            'user_surname': subscriber.surname,
            'user_birthday': subscriber.birthday,
        }
        html = mail_template.render(context)
        msg = EmailMultiAlternatives(subject='Your newsletter',
                                     body=html,
                                     from_email=settings.DEFAULT_FROM_EMAIL,
                                     to=[subscriber.email])
        msg.content_subtype = 'html'
        try:
            msg.send()
        except:
            massages_sent = False
            print 'Error'

    context = {
        'subscribers_list': subscribers_list,
        'massages_sent': massages_sent
    }
    return render(request, 'mailer/mail_template.html', context)
