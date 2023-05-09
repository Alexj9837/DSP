from django.urls import path
from custom_news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.news, name="home"),
    path('get_news', views.get_news, name='get_news'),
    path('news', views.news, name='news'),
    path('custom_news', views.custom_news, name='custom_news'),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path('add_interest/', views.add_interest, name='add_interest'),
    path('remove_interest/', views.remove_interest, name='remove_interest'),
    path('signup/', views.signup, name='signup'),
]