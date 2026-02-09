from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='product-list'),
    path('analyze/', views.analyze_cart, name='analyze-cart'),
]