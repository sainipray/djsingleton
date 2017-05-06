#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from djsingleton.models import SingletonModel, SingletonActiveModel


class Config(SingletonModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Configuration"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class APIKey(SingletonActiveModel):
    key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.key

    def __unicode__(self):
        return self.key

    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"
