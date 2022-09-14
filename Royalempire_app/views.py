from ast import Return
from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import available_items
from django.http import JsonResponse, response,HttpResponse
from .forms import *


def index(request):
    
    available_items_list = available_items.objects.all()
    paginator = Paginator(available_items_list,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'count':page_obj.count,
        'page_obj':page_obj,
    }
    return render(request, 'Royalempire_app/index.html', context)

def items_add(request):
    available_table = available_items()

    if request.method == 'POST':
        available_item = available_items_form(request.POST, request.FILES, instance=available_table)
        # if available_item.is_valid():
            
        
        item_name = request.POST.get('item_name')
        item_color = request.POST.get('item_color')
        # user = request.POST.get('item_img')
        # uploadeditem_img = request.FILES['file']
        uploadeditem_img = request.POST.get('item_img')
        
               
        available_items.objects.create(item_name=item_name, item_color=item_color, item_img=uploadeditem_img)
        
        # available_item.save()
        
    #     return HttpResponse('item created')
    # else:
    #     available_item = available_items_form
    #     return HttpResponse('Error Code 500 ')
    
    available_items_list = available_items.objects.all()
    paginator = Paginator(available_items_list,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'available_item':available_item,
        'count':page_obj.count,
        'page_obj':page_obj,
    }
    return render(request,'Royalempire_app/pagination.html',context)
    
def base(request):
    return render(request, 'Royalempire_app/base.html',None)

def pagination(request):
    return render(request, 'Royalempire_app/pagination.html',None)

def check_field(request):
    Item_name = request.POST.get('item_name')
    if available_items.objects.filter(item_name=Item_name).exists(): 
        return HttpResponse("<div id='check_trans' class='success text-red-500 px-6 '>item already exist</div>")
    else:
        return HttpResponse("<div id='check_trans' class='error text-green-500 px-6 '>item available<div>")

# def paginated_img(request):
    # available_items_list = available_items.objects.all()
    # paginator = Paginator(available_items_list,1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    # context = {
        
    # }
    # return render(request, 'Royalempire_app/index.html', context)

def search_sect(request):
    search_item = request.POST.get('search')
    results = available_items.objects.filter(item_name__contains=search_item)
    context = {
        'results':results,
    }
    return render(request, 'Royalempire_app/search_result.html', context)

def add_search(request):
    gotten_name = request.POST.get('item_name')
    selected.objects.create(item_name=gotten_name)
    # available_items.objects.get_or_create(item_name=gotten_name)
    context={
        
    }
    return render(request, 'Royalempire_app/search_result.html',context)

def items_display(request):
    context={
        
        }
    
    return render(request,'Royalempire_app/items_display.html',context)

def landingpage(request):
    context = {}
    return render(request,'Royalempire_app/landingpage.html',context)