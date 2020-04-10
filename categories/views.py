from django.shortcuts import render, redirect
from .models import Category
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def category_list(request):
    categories = Category.objects.all().order_by("title")
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required(login_url="/accounts/login/")
def category_create(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            form.save()
            return redirect('categories:list')
    else:
        form = forms.CategoryForm()
    return render(request, 'categories/category_create.html', {'form': form})

@login_required(login_url="/accounts/login/")
def category_edit(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            # save to db
            form.save()
            return redirect('categories:list')
    else:
        form = forms.CategoryForm(instance=category)
    return render(request, 'categories/category_edit.html', {'category': category, 'form': form})

@login_required(login_url="/accounts/login/")
def category_delete(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    
    return render(request, 'categories/category_delete.html', {'category': category})