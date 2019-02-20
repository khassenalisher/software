from django.urls import path
from . import views

app_name = 'tb_searcher'

urlpatterns = [
    path('', views.searchResult, name="searchResult"),
]
