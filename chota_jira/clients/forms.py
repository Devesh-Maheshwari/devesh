from django import forms
from .models import Company,Project,Projectmodule,User
from django.contrib.auth.forms import UserCreationForm


class NameForm(forms.ModelForm):
    class Meta:
        model = Company
        fields='__all__'




class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['email'].widget.attrs['readonly'] = True

    def clean_email(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            return instance.email
        else:
            return self.cleaned_data['email']

    class Meta:
         model = User
         fields=('emp_code','emp_name','salary','email','emp_mobile')





class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields='__all__'

	"""docstring for Project"""
	


class projectmodform(forms.ModelForm):
	class Meta:
		model = Projectmodule
		fields='__all__'




class UserForm(UserCreationForm):

	class Meta:
		model=User
		fields=('username','email','password1','password2','role','emp_code')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.PasswordInput()


