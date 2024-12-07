from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('url_shortener/', views.ShortenURLView.as_view(), name='shorten_url'),
    path('stats/', views.URLStatsView.as_view(), name='stats'),
    path('stats/<str:short_url>/', views.URLstats.as_view(), name='url_stats'),
    path('url_shortener/vip/', views.CustomShortenedURLAPIView.as_view(), name='custom_shorten_url'),
    path('<str:short_url>/', views.RedirectURLView.as_view(), name='redirect_url'),
]