from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import CharField, Form, ModelForm
from poem_gen.models import CustomUser, Line

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class GeneratePoemForm(Form):
    first_char = CharField(max_length=1)
    second_char = CharField(max_length=1)
    third_char = CharField(max_length=1)

class WriteLineForm(ModelForm):
    class Meta:
        model = Line
        fields = ['content']
