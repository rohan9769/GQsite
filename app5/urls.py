from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('welcome',views.welcome,name='welcome'),
    #path('imgflip',views.imgflip,name='imgflip'),
    path('geo',views.geo,name='geo'),
    path('api',views.api,name='api')
]