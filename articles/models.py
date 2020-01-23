from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def snippet(self):
        contents = str(self.body)
        if len(contents) > 50:
            contents = contents[:50] + "..."
        return contents