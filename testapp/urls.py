from django.contrib import admin
from django.urls import path, include #追加


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app.urls")) #追加
]