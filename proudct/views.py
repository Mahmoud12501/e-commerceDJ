from django.shortcuts import render
from .models import Proudct,ProudctImge,Brand,Category
from django.views.generic import ListView,DetailView
from django.db.models import Count
# Create your views here.

class ProudctListView(ListView):
    model=Proudct
    

class ProudctDetailView(DetailView):
    model = Proudct
    
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myProudct=self.get_object()
        context['imges']=ProudctImge.objects.filter(proudct=myProudct)
        return context
  


class BrandListView(ListView):
    model = Brand
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"]=Brand.objects.all().annotate(proudct_count=Count('product_brand'))
        return context



class BrandDetailView(DetailView):
    model = Brand
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproudct=self.get_object()
        context["brand_proudct"]=Proudct.objects.filter(brand=myproudct)
        return context


class CategoryListView(ListView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category']=Category.objects.all().annotate(category_count=Count('product_category'))
        return context
    
    


