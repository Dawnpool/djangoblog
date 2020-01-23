from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('search/', views.search_result, name="search"),
    path('<slug:slug>/', views.article_details, name="detail"),
]
