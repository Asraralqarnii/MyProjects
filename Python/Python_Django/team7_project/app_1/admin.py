from django.contrib import admin
from .models import Post,Category
admin.site.register(Post)
admin.site.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'body', 'image')