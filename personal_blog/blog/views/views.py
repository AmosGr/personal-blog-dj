from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib import messages
from ..forms.creat_post_form import PostForm
from django.contrib.auth.models import User
from ..models.post import Post


# Create your views here.
def welcome(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            author_username = form.cleaned_data['author']
            author = User.objects.get(username=author_username)
            new_post.author = author
            new_post.save()
            messages.success(request, 'Post criado com sucesso!')
            return render(request, 'welcome.html', {'form': PostForm(), 'new_post':  Post.objects.filter(status=1)})
        else:
            messages.error(request, 'Falha ao criar post. Por favor, corrija os erros abaixo.')
    else:
        form = PostForm()

    published_posts = Post.objects.filter(status=1)
    return render(request, 'welcome.html', {'form': form, 'published_posts': published_posts})


def welcome_(request):
    published_posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'welcome.html', {'published_posts': published_posts})

# def welcome(request): 
    
#     if request.method == 'POST':
#         new_post = Post()
#         new_post.title = request.POST['title']
#         new_post.author = request.POST['author']
#         new_post.content = request.POST['content']
#         new_post.status = request.POST['status']

#         try: 
#             new_post.create()
#             messages.success(request,' Post criado com sucesso!')
#             return render(
#                 request=request, 
#                 template_name='welcome.html', 
#                 context={'title': new_post.title, 'author': new_post.author, 'content': new_post.content, 'status': new_post.status}
#             )
#         except ValidationError as e: 
#             messages.error(request, f'Falha ao criar post: {e}')
#     return render(request=request, 
#                   template_name='welcome.html')


# title 
# slug 
# author
# update_on 
# content 
# reated_on 
# status
