from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=20, null=False)
  password = models.CharField(max_length=15, null=False)
  gender = models.CharField(max_length=1, null=False)
  country = models.CharField(max_length=25, null=True)

class PublicationHouse(models.Model):
  name = models.CharField(max_length=50, null=False)
  ratings = models.IntegerField(null=True)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=50, null=False)
  pages = models.IntegerField(null=False)
  price = models.FloatField(null=True, blank=True)
  published = models.DateField(null=True, default=date.today())
  publicationhouse = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)

  # magic field
  # review_set

  def __str__(self):
      return self.title

class Review(models.Model):
  reviewer = models.CharField(max_length=50, null=False)
  description = models.CharField(max_length=100, null=False)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)