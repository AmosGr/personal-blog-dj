from django import forms
from ..models.post import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'status']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 10,  # Defina o número inicial de linhas
                'cols': 80,  # Defina a largura inicial
                'style': 'resize:none;',  # Impede redimensionamento manual (opcional)
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].choices = [(user.id, user.get_full_name()) for user in User.objects.all()]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['author'].choices = [(user.id, user.get_full_name()) for user in User.objects.all()]