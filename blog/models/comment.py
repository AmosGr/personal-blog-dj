from django.db import models
from .post import Post
from django.utils import timezone


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return 'Comment {} by {}.'.format(self.body, self.name)
