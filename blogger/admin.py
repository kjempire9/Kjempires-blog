from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author_username', 'title')
    prepopulated_fields = {'slug' : ('title',)}
    list_editable = ('status',)
    date_hierachy = ('created',)

admin.site.site_header = 'screenshots254 administration'
admin.site.site_title = 'Johnny site admin'
admin.site.register(Post, PostAdmin)
