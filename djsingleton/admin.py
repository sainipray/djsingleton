#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


class SingletonAdmin(admin.ModelAdmin):
    actions = None

    def __init__(self, model, admin_site):
        fields = [field.name for field in model._meta.fields]
        self.list_display = fields[:5]
        self.list_display_links = fields[:5]
        super(SingletonAdmin, self).__init__(model, admin_site)

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SingletonActiveAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        fields = [field.name for field in model._meta.fields]
        self.list_display = fields[:5]
        self.list_display_links = fields[:5]
        self.list_filter = ['active']
        super(SingletonActiveAdmin, self).__init__(model, admin_site)
