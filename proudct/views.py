from django.shortcuts import render
from .models import Proudct
from django.views.generic import ListView,DetailView
# Create your views here.

class ProudctListView(ListView):
    model=Proudct
    

class ProudctDetailView(DetailView):
    model = Proudct
    
