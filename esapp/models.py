from django.db import models
from django.utils import timezone
from .search import BlogPostIndex

from django.contrib.auth.models import User


# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    posted_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)

    def indexing(self):
       obj = BlogPostIndex(
          meta={'id': 1240, 'score': 10},
          author=self.author.username,
          posted_date=self.posted_date,
          title=self.title,
          text=self.text
       )
       print(obj.save())
       return obj.to_dict(include_meta=True)    