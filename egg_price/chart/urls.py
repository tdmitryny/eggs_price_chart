from django.urls import path
from . import views  # Ensure views are correctly imported

urlpatterns = [
    path('', views.Chart.as_view(), name='chart'),
]