from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENRE = (
    ('HO', 'Horror'),
    ('CO', 'Comedy'),
    ('WE', 'Western'),
    ('RO', 'Romantic'),
    ('AC', 'Action')
)


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_genre = forms.CharField(label="What is your favorite move genre", widget=forms.Select(choices=GENRE))
	second_genre = forms.CharField(label="What is your favorite move genre", widget=forms.Select(choices=GENRE))
	third_genre = forms.CharField(label="What is your favorite move genre", widget=forms.Select(choices=GENRE))
	class Meta:
		model = User
		fields = ["username", "email", "first_genre", "second_genre", "third_genre"]