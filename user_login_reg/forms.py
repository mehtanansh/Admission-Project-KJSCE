from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.db import models
from django.contrib.auth import password_validation

from .models import Applicant, User, Verifier

class VerifierRegisterForm(UserCreationForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username *'}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email *'}))
	password1 = forms.CharField(
		strip=False,
		label='',
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
		help_text=password_validation.password_validators_help_text_html())
	password2 = forms.CharField(
		strip=False, label='',
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Confirmation'}),
		help_text='<ul><li>Your password should match the one entered in the previous field.</li></ul')

	class Meta:
		unique_together = (('email',),
						   ('mobilenum'))
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	@transaction.atomic
	def save(self):
		user = super().save(commit = False)
		user.is_verifier = True
		user.save()
		verifier = Verifier.objects.create(username = user)
		return user

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name *'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name *'}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email *'}))
	dob = forms.DateField(label='', widget=forms.DateInput(attrs={'class':'form-control','placeholder':'mm/dd/yyyy *'}))
	mobilenum = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number *'}))
	password1 = forms.CharField(
		strip=False,
		label='',
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
		help_text=password_validation.password_validators_help_text_html())
	password2 = forms.CharField(
		strip=False, label='',
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Confirmation'}),
		help_text='<ul><li>Your password should match the one entered in the previous field.</li></ul')

	class Meta:
		unique_together = (('email',),
						   ('mobilenum'))
		model = User
		fields = ['first_name', 'last_name', 'email', 'mobilenum', 'dob', 'password1', 'password2']

	@transaction.atomic
	def save(self):
		user = super().save(commit = False)
		user.is_student = True
		user.save()
		applicant = Applicant.objects.create(applId = user)
		return user

class OTPForm(forms.Form):
	mob_otp = forms.CharField(label="mob")
	email_otp = forms.CharField(label="email")

