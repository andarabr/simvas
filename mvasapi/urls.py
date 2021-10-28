from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    path('reports/', views.index, name='index-report'),
    # path('about/', views.about, name='blog-about'),
]