#-*- coding: utf-8 -*-
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class BookInstanceAdminForm(forms.ModelForm):
    """ Form for validation of bookinstance in admin."""

    def clean(self):
        cleaned_data = super().clean()
        issued_to = cleaned_data['issued_to']
        status = cleaned_data['status']
        #Validation of status and book receiever
        if issued_to == None and status == 'o':
            raise ValidationError(_('Invalid:Status can\'t be on loan. Issued to field is empty.'))
        if issued_to != None and status != 'o':
            raise ValidationError(_('Book can\'t be issued if the status is not on loan.'))
        if status == 'd' and issued_to == None:
            raise ValidationError(_('A book can\'t be due as Issued to field is empty.'
            ))
            
    