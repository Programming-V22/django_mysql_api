from django.urls import path
from .views import ProductoView

urlpatterns = [
    path('productos/', ProductoView.as_view(), name='product_list'),
    path('productos/<int:id>', ProductoView.as_view(), name='product_proccess')
]
