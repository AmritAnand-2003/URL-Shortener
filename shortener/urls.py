from django.urls import path
from . import views

urlpatterns = [
    path('url_shortener/', views.ShortenURLView.as_view(), name='shorten_url'),
    path('<str:short_url>/', views.RedirectURLView.as_view(), name='redirect_url'),
    path('<str:short_url>/stats/', views.URLstats.as_view(), name='stats'),
]