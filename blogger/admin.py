from django.contrib import admin
from .models import Post, Profile, Images, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author_username', 'title')
    prepopulated_fields = {'slug' : ('title',)}
    list_editable = ('status',)
    date_hierachy = ('created',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.site_header = 'screenshots254 administration'
admin.site.site_title = 'Johnny site admin'
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Images, ImagesAdmin)
