from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage


class HomeAdmin(PageAdmin):
    inlines = (HomePage,)
    fieldsets = deepcopy(PageAdmin.fieldsets)


    admin.site.register( HomePage,)