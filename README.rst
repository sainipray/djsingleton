===============
Djsingleton
===============

This is useful for create singleton model in django for make global settings.

.. image:: https://img.shields.io/pypi/v/djsingleton.svg
    :target: https://pypi.python.org/pypi/djsingleton

.. image:: https://api.travis-ci.org/sainipray/djsingleton.svg
    :target: https://travis-ci.org/sainipray/djsingleton/

.. image:: https://img.shields.io/pypi/pyversions/djsingleton.svg
    :target: https://travis-ci.org/sainipray/djsingleton/

Overview
========

- SingletonModel - User can work with global settings using singletons.

- SingletonActiveModel - User can save multiple entries but always one entry will active and work as global settings.

Documentation
=============

- Installation -
   * Run ::

      pip install djsingleton

   * Add 'djsingleton' to your INSTALLED_APPS ::

      'djsingleton',

- Customization -
   * Inherit  'SingletonModel', 'SingletonActiveModel' in your model ::

       from djsingleton.models import SingletonModel, SingletonActiveModel

       class Config(SingletonModel):
           name = models.CharField(max_length=255, null=True, blank=True)

       class APIKey(SingletonActiveModel):
           key = models.CharField(max_length=255, null=True, blank=True)

   * Inherit 'SingletonAdmin', 'SingletonActiveAdmin' in your admin class of model ::

      from djsingleton.admin import SingletonAdmin, SingletonActiveAdmin
      admin.site.register(Config, SingletonAdmin)
      admin.site.register(APIKey, SingletonActiveAdmin)

   * In Templates {% load 'djsingleton' %} ::

      {% load 'djsingleton' %}
      {% get_singleton 'main' 'Config' as object %}
      {{ object.name }}

      {% get_singleton 'main' 'APIKey' as object %}
      {{ object.key }}

   Above 'main' > App Label and 'Config' or 'APIKey' > Model Name

   Note: In 'SingletonActiveModel' model, You can't delete active row from model. You have to active another row if you want to delete.
License
=======

Djsingleton is an Open Source project licensed under the terms of the `MIT license <https://github.com/sainipray/djsingleton/blob/master/LICENSE>`_
