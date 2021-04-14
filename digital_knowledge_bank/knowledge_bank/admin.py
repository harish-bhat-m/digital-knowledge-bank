from django.contrib import admin
from .models import Tag, Post

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',) 
    list_filter = ('tag_name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {'slug': ('author','title',)}
    list_filter = ("title",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
