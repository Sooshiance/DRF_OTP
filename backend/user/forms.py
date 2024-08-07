from django import forms

from user.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
