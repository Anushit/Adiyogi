from django import forms
from .models import Employee,State,City,Post
from django.contrib.auth.models import User
from django.utils.translation import ugettext
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username','firstname','lastname','email','password','country','state','city']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = Employee.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError("invaild user loggin")
        return username

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'firstname', 'lastname', 'email','country','state','city']

class AddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username','firstname','lastname','email','country','state','city']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ForgetPassForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Employee
        fields = ('email',)

    def clean(self):
        cleaned_data = super(ForgetPassForm, self).clean()
        email = cleaned_data.get("email")

        if not Employee.objects.filter(email=email).exists():
            raise forms.ValidationError(
               ugettext("This email address does not exist in database.!")
            )

class password_reset(forms.Form):
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class EditUserForm(forms.Form):
    class Meta:
        model = Employee
        fields = ['username','email','image']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_description','meta_description','content','image']