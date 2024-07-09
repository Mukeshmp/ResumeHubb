from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Query the MySQL database to check if the user exists and the password is correct
        user = user.objects.filter(uemail=username, upass=password).first()
        if not user:
            raise forms.ValidationError("Invalid username or password")
