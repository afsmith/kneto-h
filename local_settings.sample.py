# Make this unique, and don't share it with anybody.
SECRET_KEY = 'acb_d1jb)*)asg1161!#"&!0hjq9z$cg-l3*z*4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kneto_dev',
        'USER': 'kneto_dev',
        'PASSWORD': 'kneto_dev',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Helsinki'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
