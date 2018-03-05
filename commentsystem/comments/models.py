from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    comments=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='posts')

    def __str__(self):
        return self.comments

class Comments(models.Model):
    post=models.ForeignKey(Posts,related_name='comments')
    commments=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='comments')
    updated_by=models.ForeignKey(User,related_name='+')
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comments
