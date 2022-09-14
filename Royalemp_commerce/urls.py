from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.store, name='store'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),
    path('views', views.views, name='views'),
    path('updateItem', views.updateItem, name='updateItem'),
]

htmx_urlpatterns = [
    path('store_cart', views.store_cart, name='store_cart'),
    
]

urlpatterns += htmx_urlpatterns