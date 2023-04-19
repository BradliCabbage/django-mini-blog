from django.db import models


# Create your models here.
from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
  name = models.ForeignKey(User, on_delete=models.CASCADE)
  bio = models.CharField(
    max_length=200, help_text="Write a short bio for the author"
  )

  def get_absolute_urls(self):
    """Returns the url to access a particular Author instance"""
    return reverse("author-detail", args=[str(self.id)])

  def _str_(self):
    """String for representing the model object"""
    return f"{self.title}"

class Blog(models.Model):
  """Model representing blog posts"""
  title = models.CharField(max_length=200)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.CharField(max_length=1500)
  
  post_date = models.DateField(null=True, blank=True)
  body = models.TextField()

  def get_absolute_urls(self):
    """Returns the url to access a particular blog instance"""
    return reverse("blog-detail", args=[str(self.id)])
    
  def _str_(self):
    """String for representing the model object"""
    return f"{self.title}"


class BlogComment(models.Model):
  """Model representing the blog comments"""

  author = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.CharField(max_length=500)
  post_date = models.DateField(null=True, blank=True)
  blog = models.ForeignKey("Blog", on_delete=models.SET_NULL, null=True )

  def _str_(self):
    """String for representing the model object"""
    return f"{self.description}"
