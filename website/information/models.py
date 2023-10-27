from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

LANGUAGES = (
    ('en', 'English'),
    ('tel', 'Telugu'),
    ('hindi', 'Hindi'),
    ('tamil', 'Tamil'),
)

COUNTRY = (
    ('IND', "INDIA"),
    ('JAP', "JAPAN"),
    ("RUS", "RUSSIA"),
    ('USA', "AMERICA")
)

GENERE = (
    ("action", "action"),
    ("comedy", "comedy"),
    ("thriller", "thriller"),
    ('romantic', 'romantic'),
    ('horror', 'horror'),
    ('drama', 'drama'),
)


class Movie(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=10, choices=LANGUAGES, default="tel")
    director_name = models.CharField(max_length=20)
    hero_name = models.CharField(max_length=20)
    genere = models.CharField(max_length=40,choices=GENERE)
    country = models.CharField(max_length=10, default="IND", choices=COUNTRY)
    streaming_platform = models.CharField(max_length=20)
    release_date = models.DateField(auto_now_add=True)
    budget = models.CharField(max_length=10)
    runtime = models.DurationField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name