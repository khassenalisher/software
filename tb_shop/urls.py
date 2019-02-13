from django.urls import path
from . import views

app_name = 'tb_shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdutcs'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
]