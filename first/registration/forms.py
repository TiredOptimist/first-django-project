from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import NewUser


class UniqueValidator:
    def __init__(self, queryset, field):
        self.queryset = queryset
        self.field = field

    def __call__(self, value):
        if self.queryset.filter(**{self.field: value}).exists():
            raise ValidationError(f"This {self.field} is already taken.")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        validators=[UniqueValidator(NewUser.objects.all(), "email")],
    )

    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = ("username", "email")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        }
        validators = {
            "username": UniqueValidator(NewUser.objects.all(), "username"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
        self.fields["password2"].widget = forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('email', 'avatar', 'status')
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль:", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль:", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля:", widget=forms.PasswordInput(attrs={'class': 'form-input'}))