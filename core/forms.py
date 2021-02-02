from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


GENRE = (
    ('HO', 'Horror'),
    ('CO', 'Comedy'),
    ('WE', 'Western'),
    ('RO', 'Romantic'),
    ('AC', 'Action')
)

class MyCustomSignupForm(SignupForm):

	def __init__(self, *args, **kwargs):
		super(MyCustomSignupForm, self).__init__(*args, **kwargs)
		self.fields['organization'] = forms.CharField(required=True)
	
	def save(self, request):
		organization = self.cleaned_data.pop('organization')
		user = super(MyCustomSignupForm, self).save(request)

# class MyCustomSignupForm(SignupForm):
# 	email = forms.EmailField()
# 	first_genre = forms.CharField(label="What is your favorite move genre", widget=forms.Select(choices=GENRE))
# 	second_genre = forms.CharField(label="What is your favorite move genre", widget=forms.Select(choices=GENRE))
# 	third_genre = forms.CharField(label="What is your favorite move genre", widget=forms.Select(choices=GENRE))
# 	class Meta:
# 		model = User
# 		fields = ["username", "email", "first_genre", "second_genre", "third_genre"]
