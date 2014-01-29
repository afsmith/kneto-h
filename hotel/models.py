from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    acctop = models.CharField(max_length=500,
        help_text="cms managed text", default="cms text")
    
    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")

