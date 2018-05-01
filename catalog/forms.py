from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class RenewItem (forms.Form):
	renewal_date = forms.DateField()
