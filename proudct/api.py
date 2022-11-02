from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Proudct,Brand,Test
from .serializers import ProudctSerializer,BrandSerializer,TestSerializer,CategorySerializer
from django.db.models.functions import Power
from rest_framework import status, filters
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins,viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated 

@api_view(['GET','POST'])
def proudct_list_api(request):
    
    if request.method=='GET':
        proudcts=Proudct.objects.all()[:20]
        # proudcts=Proudct.objects.annotate(is_new=Power('price',2))[:10]
        serializer=ProudctSerializer(proudcts,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        form=ProudctSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return Response(form.data)
        return Response(form.data,status=400)
        

@api_view(['GET','POST'])
def brand_list_api(request):
    
    if request.method=='GET':
        brands=Brand.objects.all()[:20]
        # proudcts=Proudct.objects.annotate(is_new=Power('price',2))[:10]
        serializer=BrandSerializer(brands,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        form=BrandSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return Response(form.data)
        return Response(form.data,status=400)
@api_view(['PUT','GET'])        
def add_pro(request,pk):
     proudct = Proudct.objects.get(pk=pk)
     if request.method == 'GET':
        serializer = ProudctSerializer(proudct)
        return Response(serializer.data)
     elif request.method == 'PUT':
        serializer = ProudctSerializer(proudct, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

class Api_list(generics.ListCreateAPIView):
    queryset = Proudct.objects.all()[:10]
    serializer_class = ProudctSerializer
    

@api_view(['GET','POST'])
def test_list_api(request):
    
    if request.method=='GET':
        test=Test.objects.all()[:20]
        # proudcts=Proudct.objects.annotate(is_new=Power('price',2))[:10]
        serializer=TestSerializer(test,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        form=TestSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return Response(form.data)
        return Response(form.data,status=400)

@api_view(['GET','PUT','DELETE'])
def test_pk_api(request,pk):
    test=Test.objects.get(pk=pk)
    
    if request.method=='GET':
        serializer=TestSerializer(test).data
        return Response(serializer,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        form=TestSerializer(test,data=request.data)
        if form.is_valid():
            form.save()
            return Response(form.data,status=status.HTTP_202_ACCEPTED)
        elif request.method=="DELETE":
            test.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
#__________________________________________________________________________#   
# CBV
class Test_list(APIView):
    def get(self,request):
        test=Test.objects.all()
        serailizer=TestSerializer(test,many=True).data
        return Response(serailizer,status=status.HTTP_200_OK)
    def post(self,request):
        serailizer=TestSerializer(request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class Test_pk(APIView):
    def get_object(self,pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404
        
    def get (self,request,pk):
        test=self.get_object(pk)
        serializer=TestSerializer(test).data
        return Response(serializer,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        test=self.get_object(pk)
        serailzer=TestSerializer(test,data=request.data)
        if serailzer.is_valid():
            serailzer.save()
            return Response(serailzer.data,status=status.HTTP_202_ACCEPTED)
        
    def delete(self,request,pk):
        test=self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Test.objects.all()
    serializer_class=TestSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Test.objects.all()
    serializer_class=TestSerializer
    
    def retrive(self,request,pk):
        return self.retrieve(request).data
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)
    

class generc_list(generics.ListCreateAPIView):
     queryset=Test.objects.all()
     serializer_class=TestSerializer
     
class generc_pk(generics.RetrieveUpdateDestroyAPIView):
     queryset=Test.objects.all()
     serializer_class=TestSerializer
#__________________________________________________________________________#   
     
class ProudctViewsets(viewsets.ModelViewSet):
    #  authentication_classes=[BasicAuthentication]
    #  permission_classes=[IsAuthenticated]
     queryset=Proudct.objects.all()
     serializer_class=ProudctSerializer
    #  filter_backends=(filters.SearchFilter)
    #  sea
class BrandViewsets(viewsets.ModelViewSet):
     queryset=Brand.objects.all()
     serializer_class=BrandSerializer
     
class CategoryViewsets(viewsets.ModelViewSet):
     queryset=Category.objects.all()
     serializer_class=CategorySerializer
     
@api_view(['GET'])
def searche_proudct(request):
    proudct=Proudct.objects.filter(price=request.data['price'])
    serailizer=ProudctSerializer(proudct,many=True).data
    return Response(serailizer,status=status.HTTP_200_OK)