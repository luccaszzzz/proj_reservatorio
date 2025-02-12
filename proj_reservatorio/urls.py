from django.contrib import admin
from django.urls import path
from core.views import home, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login, name="login"),
]
