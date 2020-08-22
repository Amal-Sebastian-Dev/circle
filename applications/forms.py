# Forms related to the applications app

from django import forms

from .models import Application, Scheme
from . import choices

class ApplySchemeForm(forms.Form):
	
	category = forms.ChoiceField(
		choices = choices.depts,
		widget = forms.Select(attrs={
				'class' : 'form-control',
				'required' : '',
		}),
	)
	
	scheme = forms.ModelChoiceField(
		queryset = Scheme.objects.all(),
		widget = forms.Select(attrs = {
			'class' : 'form-control',
			'required' : '',
		})
	)
	district = forms.ChoiceField(
		choices = choices.districts,
		widget = forms.Select(attrs = {
			'class' : 'form-control',
			'required' : '',
		})
	)
	office_type = forms.ChoiceField(
		choices = choices.office_types,
		widget = forms.Select(attrs = {
			'class' : 'form-control',
			'required' : '',
		})
	)
	location = forms.ChoiceField(
		choices = choices.locations,
		widget = forms.Select(attrs = {
			'class' : 'form-control',
			'required' : '',
		})
	)
	application_type = forms.ChoiceField(
		choices = choices.application_types,
		widget = forms.Select(attrs = {
			'class' : 'form-control',
			'required' : '',
		})
	)
	
