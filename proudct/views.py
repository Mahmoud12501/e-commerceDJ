
from django.shortcuts import render
from .models import Proudct,ProudctImge,Brand,Category,ProudctReview
from django.views.generic import ListView,DetailView
from django.db.models import Count , Q , F,Value
from django.db.models.functions import Power
from django.db.models.aggregates import Max,Sum
from .forms import ReviewForm

# Create your views here.

def all_proudct(request):
    # objects=Proudct.objects.filter(price__gte=90)
    # objects=Proudct.objects.filter(category__id__function=90)
    # objects=Proudct.objects.filter(name__contains="ahmed")
    # objects=Proudct.objects.filter(quantiy=F('price'))
    # objects=Proudct.objects.order_by("name")
    # objects=Proudct.objects.latest("name")
    # objects=Proudct.objects.prefetch_related('category').all()
    # objects=Proudct.objects.annotate(is_new=Value(True))
    # objects=Proudct.objects.only("name",'price')
    # objects=Proudct.objects.annotate(is_new=Power('price',0))
    # objects=Proudct.ad_manger.all()
    objects=Proudct.ad_manger.only("name",'price')

    return render(request,"proudct/all_proudct.html",{"proudcts":objects})


class ProudctListView(ListView):
    model=Proudct
    paginate_by=100

class ProudctDetailView(DetailView):
    model = Proudct
    
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myProudct=self.get_object()
        context['imges']=ProudctImge.objects.filter(proudct=myProudct)
        context['related']=Proudct.objects.filter(category=myProudct.category)[:20]
        context["reviews"]=ProudctReview.objects.filter(proudct=myProudct)
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
        context["brand_proudcts"]=Proudct.objects.filter(brand=myproudct)
        context["brands"]=Brand.objects.all().annotate(proudct_count=Count('product_brand'))

        return context


class CategoryListView(ListView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys']=Category.objects.all().annotate(proudct_count=Count('product_category'))
        return context
    
    

class CategoryDetailView(DetailView):
    model = Category
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproudct=self.get_object()
        context["category_proudct"]=Proudct.objects.filter(category=myproudct)
        
        return context


from django.http import JsonResponse
from django.template.loader import render_to_string 

def add_review(request,id):
    print("---------------------------------------------------")
    print(request.POST)
    proudct=Proudct.objects.get(id=id)
    print("---------------------------------------------------")
    if request.method =="POST":
        print("$"*20)
        form=ReviewForm(request.POST)
        print("$"*20)
        if form.is_valid():
            print("$"*20)
            myform=form.save(commit=False)
            myform.user=request.user
            myform.proudct=proudct
            myform.save()
            
            reviews=ProudctReview.objects.filter(proudct=proudct)
            html=render_to_string("include/reviews.html",{"reviews":reviews, request:request})
            return JsonResponse({'result':html})
        
class ProudctDetailView2(DetailView):
    model = Proudct
    template_name="proudct/ajax.html"