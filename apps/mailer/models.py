# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.EmailField(max_length=100)
