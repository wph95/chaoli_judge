# coding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import AppendedText, PrependedText
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, TextInput, EmailInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit ,MultiField , Div
from crispy_forms.bootstrap import AppendedText, PrependedText



class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'placeholder': '用户名/邮箱',
                                         'required': 'required',
                                         'class': 'form-control no-border',
                                        }

                    ),
            'password': PasswordInput(attrs={'placeholder': '密码',
                                             'required': 'required',
                                             'class': 'form-control no-border',
                                            }
                                      )
                    }
        help_texts = {
        #    'username': ('The description of this interview question'),
        }
        error_messages = {
            'password': {
                'empty': ("Your description is empty."),
            },
        }