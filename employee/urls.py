from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', views.index, name='index-employee'),
    # path('about/', views.about, name='blog-about'),
]