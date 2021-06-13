from django.urls import path
from .views import HomePageView,AboutPageView, KurslarPageView,ContactPageView
urlpatterns=[
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('kurslar/', KurslarPageView.as_view(),name='kurslar'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('',  HomePageView.as_view(), name='home')
]