from django.contrib import admin

# Register your models here.
from .models.post import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title','author')}




# Adding Post model on admin page. 
admin.site.register(Post,PostAdmin)