from django.urls import path
from . import views

app_name = 'scheduleapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/', views.PostView.as_view(), name='post'),
]