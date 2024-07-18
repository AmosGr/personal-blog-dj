from django.contrib.auth.models import User
from django.db import models


STATUS = ((0, 'Rascunho'),
          (1, 'Publicar')
          )


class Post(models.Model):
    "Create a table on database to Post model on blog."

    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)

    class Meta:
        """Metaclass to configure additional options for the Post model.
        You can set the ordering in two ways:
            - descending: ['-xyz']
            - ascending: ['xyz']

        """
        ordering = ['-created_on']

    def __str__(self) -> str:
        return f'Author: {self.author} | Created on: {self.created_on}\nTitle: {self.title}'