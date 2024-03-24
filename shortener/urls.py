from django.urls import path
from .views import ShortenURL, RedirectView, SchortnerList


urlpatterns = [
    path('shortners/', SchortnerList.as_view(), name='shorten_url'),
    path('shorten/', ShortenURL.as_view(), name='shorten_url'),
    path('<str:short_id>/', RedirectView.as_view(), name='redirect'),
]