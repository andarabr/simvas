from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    path('reports/', views.index, name='index-report'),
    path('reports-history/', views.history, name='history-report'),
    # path('about/', views.about, name='blog-about'),
    path('api-test/', views.api_test, name='api-test'),
    path('api-test/<int:id>/<str:username>', views.api_test_idv, name='api-test-idv'),
]