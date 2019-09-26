from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(default='default.png')
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
        db_table = "post"
    
    def __str__(self):
        return self.title