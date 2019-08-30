from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blogger import views
from django.conf import settings
from django.conf.urls.static import static

app_name='blogger'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogger.urls')),
    path('login/', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),
    path('', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace="social")),
    path('like/', views.like_post, name="like_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
