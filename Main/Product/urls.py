from django.urls import include, path
from . views import ProductListAPIView, CategoryListAPIView, ProductDetailAPIView, ProductUpdateAPIView, ProductDeleteAPIView, CategoryDetailAPIView,CategoryUpdateAPIView,CategoryDeleteAPIView, CategoryCreateAPIView,ProductCreateAPIView




urlpatterns = [
    path('category/',CategoryCreateAPIView.as_view()),
    path('product/',ProductCreateAPIView.as_view()),
    path('products/list', ProductListAPIView.as_view()),
    path('categories/list', CategoryListAPIView.as_view()),
    path('products/<int:pk>',ProductDetailAPIView.as_view()),
    path('products/<int:pk>/update', ProductUpdateAPIView.as_view()),
    path('products/<int:pk>/delete',ProductDeleteAPIView.as_view()),
    path('categories/<int:pk>',CategoryDetailAPIView.as_view()),
    path('categories/<int:pk>/update', CategoryUpdateAPIView.as_view()),
    path('categories/<int:pk>/delete', CategoryDeleteAPIView.as_view()),
    
    
]   
