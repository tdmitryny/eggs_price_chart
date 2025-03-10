from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView, FormView

# Create your views here.
# from django.http import HttpResponse


class Chart(TemplateView):
    template_name = 'chart/chart.html'