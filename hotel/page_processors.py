from django.conf import settings
from datetime import datetime    
from django import forms
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from templated_email import send_templated_mail
from mezzanine.pages.page_processors import processor_for
from .models import HomePage, HomePageContact
#import pygeoip


class HomePageForm(ModelForm):

    class Meta:
        model = HomePageContact
        widgets = {
            'form_name': forms.HiddenInput()
        }
        fields = ('email', 'form_name',)


@processor_for(HomePage)
def sign_up(request, page):
   form = HomePageForm()
   if request.method == "POST":
       form = HomePageForm(request.POST)
       if form.is_valid():
           ip = request.META.get('REMOTE_ADDR', None)
 # add later          gi4 = pygeoip.GeoIP(settings.GEO_DATA, pygeoip.STANDARD)
 #         county = gi4.country_name_by_addr(ip)
           homeForm = form.save(commit=False)
           # Form processing goes here.
           homeForm.date = datetime.now()
           homeForm.ip = ip
 #          homeForm.county = county
           homeForm.form_name = 'HomePageForm'
           homeForm.save()
           send_templated_mail(
            template_name='beta_thanks',
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list=[ homeForm.email ],
            bcc=[settings.DEFAULT_BCC_EMAIL],
            context={
            'email': homeForm.email,
            },
            )

           #redirect = request.path + "?submitted=true"
           redirect = "sign_up_thanks/"

           response = HttpResponseRedirect(redirect)
           response.set_cookie( 'email', homeForm.email )
           response.set_cookie( 'county', homeForm.county )
           return response
           #return HttpResponseRedirect(redirect)
   
   return {"form": form}