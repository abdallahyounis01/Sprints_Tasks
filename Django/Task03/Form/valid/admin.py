from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("username", "gender", "text",)


admin.site.register(Post, PostAdmin)

# Register your models here.
