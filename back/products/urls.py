from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.ProductsList.as_view()),
    path('products/<slug:category_slug>/<product_slug>/', views.ProductDetail.as_view()),

]
