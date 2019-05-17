
from __future__ import unicode_literals
from django import forms
from collections import OrderedDict
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
from . import models

class InputForm(forms.Form):
    input = forms.CharField(max_length=10)

class CostForm(forms.ModelForm):
    class Meta:
        model=models.Cost
        fields='__all__'

class TableForm(forms.ModelForm):
    class Meta:
        model=models.Table
        fields='__all__'

class WorkerForm(forms.ModelForm):
    class Meta:
        model=models.Worker
        fields='__all__'

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model=models.FoodCategory
        fields='__all__'

class FoodForm(forms.ModelForm):
    class Meta:
        model=models.Food
        fields='__all__'
