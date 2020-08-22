# Forms related to the accounts app

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms

from .models import User

class RegisterForm(UserCreationForm):
	# The form for recieving the data for authentication details (phone_no and password)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs.update({ 
			'placeholder' : 'Password',
			'class' : 'form-control',
		})
		self.fields['password2'].widget.attrs.update({
			'placeholder' : 'Repeat Password',
			'class' : 'form-control',
		})
		
	class Meta:
		model = User
		fields = ['email', 'full_name', 'aadhar_no']
		widgets = {
			'email' : forms.EmailInput(attrs={
				'placeholder' : 'Email',
				'class' : 'form-control',
			}),
			'full_name' : forms.TextInput(attrs={
				'placeholder' : 'Full Name',
				'class' : 'form-control',
			}),
			'aadhar_no' : forms.TextInput(attrs={
				'placeholder' : 'Aadhar No',
				'class' : 'form-control',
			}),
		}

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({
			'placeholder' : 'Email',
			'class' : 'form-control',
		})
		self.fields['password'].widget.attrs.update({
			'placeholder' : 'Password',
			'class' : 'form-control',
		})

class PasswordChangeForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['old_password'].widget.attrs.update({
			'placeholder' : 'Old Password',
			'class' : 'form-control',
		})
		self.fields['new_password1'].widget.attrs.update({
			'placeholder' : 'New Password',
			'class' : 'form-control',
		})
		self.fields['new_password2'].widget.attrs.update({
			'placeholder' : 'Confirm New Password',
			'class' : 'form-control',
		})
