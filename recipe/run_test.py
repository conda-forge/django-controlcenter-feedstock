import django
from django.conf import settings

settings.configure(INSTALLED_APPS=['controlcenter'])

django.setup()

import controlcenter
import controlcenter.templatetags
import controlcenter.widgets

