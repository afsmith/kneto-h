from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText
from mezzanine.core.fields import RichTextField

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    lefttop_header = models.CharField(max_length=150,
        help_text="left top header", default="header")
    lefttop_line1 = models.CharField(max_length=100,
        help_text="line1", default="line1")
    lefttop_line2 = models.CharField(max_length=100,
        help_text="line2", default="line2")
    lefttop_line3 = models.CharField(max_length=100,
        help_text="line3", default="line3")
    lefttop_line4 = models.CharField(max_length=100,
        help_text="line4", default="line4")
    lefttop_line5 = models.CharField(max_length=100,
        help_text="line5", default="line5")

    righttop_header = models.CharField(max_length=100,
        help_text="right top header", default="header")
    righttop_line1 = models.CharField(max_length=75,
        help_text="line1", default="line1")

    leftbottom_header = models.CharField(max_length=100,
        help_text="left bottom header", default="header")
    leftbottom_line1 = models.CharField(max_length=75,
        help_text="line1", default="line1")

    rightbottom_header = models.CharField(max_length=100,
        help_text="right bottom header", default="header")
    rightbottom_line1 = models.CharField(max_length=75,
        help_text="line1", default="line1")

    section1_header = models.CharField(max_length=75,
        help_text="section1 header", default="header text")
#    section1 = models.TextField(max_length=2000,
    section1 = RichTextField(blank=True)

    section2_header = models.CharField(max_length=75,
        help_text="section1 header", default="header text")
    section2 = RichTextField(blank=True)

    section3_header = models.CharField(max_length=75,
        help_text="section1 header", default="header text")
    section3 = RichTextField(blank=True)

    get_header = models.CharField(max_length=150,
        help_text="get header", default="header text")
    get_header1 = models.CharField(max_length=150,
        help_text="section1 header", default="header text")
    get_text1 = RichTextField(blank=True)
    get_header2 = models.CharField(max_length=150,
        help_text="section2 header", default="header text")
    get_text2 = RichTextField(blank=True)
    get_header3 = models.CharField(max_length=150,
        help_text="section3 header", default="header text")
    get_text3 = RichTextField(blank=True)
    get_header4 = models.CharField(max_length=150,
        help_text="section4 header", default="header text")
    get_text4 = RichTextField(blank=True)
    get_header5 = models.CharField(max_length=150,
        help_text="section4 header", default="header text")
    get_text5 = RichTextField(blank=True)
    get_header6 = models.CharField(max_length=150,
        help_text="section4 header", default="header text")
    get_text6 = RichTextField(blank=True)


    what_header = models.CharField(max_length=150,
        help_text="what header", default="header text")
    what_header1 = models.CharField(max_length=150,
        help_text="section1 header", default="header text")
    what_text1 = RichTextField(blank=True)
    what_header2 = models.CharField(max_length=150,
        help_text="section2 header", default="header text")
    what_text2 = RichTextField(blank=True)
    what_header3 = models.CharField(max_length=150,
        help_text="section3 header", default="header text")
    what_text3 = RichTextField(blank=True)
    what_header4 = models.CharField(max_length=150,
        help_text="section4 header", default="header text")
    what_text4 = RichTextField(blank=True)
    what_header5 = models.CharField(max_length=150,
        help_text="section4 header", default="header text")
    what_text5 = RichTextField(blank=True)
    what_header6 = models.CharField(max_length=150,
        help_text="section4 header", default="header text")
    what_text6 = RichTextField(blank=True)


    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")



class HomePageContact(models.Model):
    """
    model for the homepage form
    """

    form_name = models.CharField(max_length=100, default='NUL')
    date = models.DateTimeField()
    email = models.EmailField()
    ip = models.GenericIPAddressField(null=True)
    county = models.CharField(null=True, max_length=50)

    def __unicode__(self):
        return self.name