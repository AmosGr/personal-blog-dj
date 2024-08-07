from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from ..models.post import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post 
    template_name = 'post_detail.html'

    def get_object(self, queryset=None):
        author = get_object_or_404(User, username=self.kwargs['author'])
        return get_object_or_404(Post, author=author, slug=self.kwargs['slug'])