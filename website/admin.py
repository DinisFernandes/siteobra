from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'trocos','location','tarefas', 'data_post',)
    list_display_links = ('id', 'title')
    list_editable = ('trocos','location','tarefas')



admin.site.register(Post, PostAdmin)
