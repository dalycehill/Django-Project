from django.shortcuts import render, redirect
from .models import Item
from categories.models import Category
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def item_list(request):
    items = Item.objects.all().order_by("title")
    
    return render(request, 'items/item_list.html', {'items': items})

@login_required(login_url="/accounts/login/")
def item_create(request):
    categories = Category.objects.all().order_by("title")
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            form.save()
            return redirect('items:list')
    else:
        form = forms.ItemForm()
    return render(request, 'items/item_create.html', {'categories': categories, 'form': form})

@login_required(login_url="/accounts/login/")
def item_edit(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            # save to db
            form.save()
            return redirect('items:list')
    else:
        form = forms.ItemForm(instance=item)
    return render(request, 'items/item_edit.html', {'item': item, 'form': form})

@login_required(login_url="/accounts/login/")
def item_delete(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('items:list')
    
    return render(request, 'items/item_delete.html', {'item': item})