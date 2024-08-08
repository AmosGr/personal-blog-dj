from django.shortcuts import get_object_or_404,render
from django.contrib.auth.models import User
from django.views import generic
from ..models.post import Post
from ..forms import CommentForm

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# class PostDetail(generic.DetailView):
#     model = Post 
#     template_name = 'post_detail.html'

#     def get_object(self, queryset=None):
#         author = get_object_or_404(User, username=self.kwargs['author'])
#         return get_object_or_404(Post, author=author, slug=self.kwargs['slug'])
    
def post_detail(request, author, slug): 
    template_name = "post_detail.html"
    author = get_object_or_404(User, username=author)
    post = get_object_or_404(Post, author=author, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            #Cria o objeto Comment mas não salva na base de dados 
            new_comment = comment_form.save(commit=False)
            # Associa o posto atual ao comentário
            new_comment.post = post
            # Salva o comentário na base de dados 
            new_comment.save()
    else: 
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post":post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form
        },
    )