from django.urls import path
from .views import HomePageView,AboutPageView, KurslarPageView,ConnectPageView
urlpatterns=[
    path('connect/', ConnectPageView.as_view(), name='aloqa'),
    path('kurslar/', KurslarPageView.as_view(),name='kurslar'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('',  HomePageView.as_view(), name='home')
]