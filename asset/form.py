# -*- coding: utf-8 -*-
from django import forms
from asset.models import *

class HostListForm(forms.ModelForm):
    class Meta:
        model = HostList
        widgets = {
          'ip': forms.TextInput(attrs={'class': 'form-control'}),
          'hostname': forms.TextInput(attrs={'class': 'form-control'}),
          'application': forms.TextInput(attrs={'class': 'form-control'}),
          'status': forms.TextInput(attrs={'class': 'form-control'}),
          'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = "__all__"
