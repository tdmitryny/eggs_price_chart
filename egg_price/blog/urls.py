from django.urls import path
from . import views  # Ensure views are correctly imported

urlpatterns = [
    path('', views.index, name='blog_home'),
]