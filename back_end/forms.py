from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from classwork_app.models import Post

class RegistrationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class EditUserForm(UserChangeForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class CreatPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('post_title', 'post_img', 'content', 'category', 'author')


