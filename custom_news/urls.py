from django.urls import path
from custom_news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.news, name="home"),
    path('get_news', views.get_news, name='get_news'),
    path('news', views.news, name='news'),
]