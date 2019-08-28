
from django.contrib import admin
from django.urls import path, include

app_name='blogger'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogger.urls'))
]
