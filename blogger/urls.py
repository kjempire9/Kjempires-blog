from django.urls import path
from blogger import views

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



]
