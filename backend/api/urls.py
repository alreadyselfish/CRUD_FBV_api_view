from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_product_list),
    path('add/', views.add_product),
    path('<int:pk>/', views.product_changes)
]
