from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blogger import views
from django.conf import settings
from django.conf.urls.static import static
app_name='blogger'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/post_edit/', views.post_edit, name="post_edit"),
    path('<int:id>/post_delete/', views.post_delete, name="post_delete"),
    path('<int:id>/favourite_post/', views.favourite_post, name="favourite_post"),
    path('<int:id>/<slug:slug>/', views.detail, name="detail"),
    path('post_create/', views.post_create, name="post_create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('favourites/', views.post_favourite_list, name="post_favourite_list"),
    path('login/', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),
    path('', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace="social")),
    path('like/', views.like_post, name="like_post"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
