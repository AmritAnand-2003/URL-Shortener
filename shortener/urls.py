from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('url_shortener/', views.ShortenURLView.as_view(), name='shorten_url'),
    # path('home2',views.URLStatsView.as_view(), name='stats'),
    path('stats/', views.URLStatsView.as_view(), name='stats'),
    path('stats/<str:short_url>/', views.URLstats.as_view(), name='url_stats'),
    path('url_shortener/vip/', views.CustomShortenedURLAPIView.as_view(), name='custom_shorten_url'),
    # path('urlstats/', views.URLStatsView2.as_view(), name='url_stats2'),
    path('<str:short_url>/', views.RedirectURLView.as_view(), name='redirect_url'),
]