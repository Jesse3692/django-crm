from django import forms
from crm import models
from django.core.exceptions import ValidationError
import hashlib


# 注册的form
class RegForm(forms.ModelForm):
    class Meta:
        # 元类
        model = models.UserProfile  # 指定model
        fields = '__all__'