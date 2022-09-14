from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
]

htmx_urlpatterns = [
    path('check_field', views.check_field, name="check_field"),
    path('pagination', views.pagination, name="pagination"),
    path('items_add', views.items_add, name="items_add"),
    # path('paginated_img', views.paginated_img, name="paginated_img"),
    path('search_sect', views.search_sect, name="search_sect"),
    path('add_search', views.add_search, name="add_search"),
    
    path('items_display', views.items_display, name="items_display"),
    path('landingpage', views.landingpage, name="landingpage"),
    
]

urlpatterns += htmx_urlpatterns