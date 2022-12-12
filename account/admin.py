from django.contrib.admin import ModelAdmin
from django.contrib import admin
from . models import *
# Register your models here.
class PostAdmin(ModelAdmin):
    list_display=('title',  'slug', 'author',)  
    list_filter=('created_on', 'author',)
    search_fields=('title', 'body',)
    prepopulated_fields={'slug':    ('title',)}
    raw_id_fields=('author',)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Reader)
    # date_hierarchy='publish'