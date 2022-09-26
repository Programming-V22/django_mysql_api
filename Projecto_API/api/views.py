from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
import json


#from django.shortcuts import render
# Create your views here.

class ProductoView(View):
    @method_decorator(csrf_exempt)
    #metodo despachar o enviar csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            productos=list(Producto.objects.filter(id=id).values())
            if len(productos)>0:
                producto=productos[0]   
                datos={'message': "Success", 'productos': productos}
            else:
                datos={'message':'productos not found'}
            return JsonResponse(datos)

        else:
            productos=list(Producto.objects.values())
            if len(productos)>0:
                datos={'message': "Success", 'productos': productos}
            else:
                datos={'message':'productos not found'}
            return JsonResponse(datos)
        
    def post(self, request):
        jd=json.loads(request.body)
       
        Producto.objects.create(name=jd['name'],photo=jd['photo'],price=jd['price'],descriptions=jd['descriptions'],date=jd['date'])
        datos={'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        productos=list(Producto.objects.filter(id=id).values())
        if len(productos)>0:
            producto=Producto.objects.get(id=id)   
            producto.name=jd['name']
            producto.photo=jd['photo']
            producto.price=jd['price']
            producto.descriptions=jd['descriptions']
            producto.date=jd['date']
            producto.save()
            datos={'message': "Success"}

        else:
            datos={'message':'productos not found'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        productos=list(Producto.objects.filter(id=id).values())
        if len(productos)>0:
            Producto.objects.filter(id=id).delete()   
            datos={'message': "Success"}
        else:
            datos={'message':'productos not found'}
        return JsonResponse(datos)