from django.db import models

GENRE = (
    ('HO', 'Horror'),
    ('CO', 'Comedy'),
    ('WE', 'Western'),
    ('RO', 'Romantic'),
    ('AC', 'Action')
)

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    first_genre = models.CharField( max_length=5, choices=GENRE)
    second_genre = models.CharField(max_length=5, choices=GENRE)
    third_genre = models.CharField(max_length=50,choices=GENRE)

