from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    published = models.Manager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published' , 'Published')
    )
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    author = models.ForeignKey(User, related_name= 'blog_post',on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=10, choices= STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return 'profile of user {}'.format(self.user.username)
