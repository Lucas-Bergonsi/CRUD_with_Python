from django.shortcuts import render, redirect
from app.forms import bicicletasForm
from app.models import  bicicletas
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    data = {}
    search= request.GET.get('search')
    if search:
        data['db'] = bicicletas.objects.filter(marca__icontains=search)
    else:
        all = bicicletas.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = bicicletasForm()
    return render(request, 'form.html', data)

def create(request):
    form = bicicletasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = bicicletas.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = bicicletas.objects.get(pk=pk)
    data['form'] = bicicletasForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = bicicletas.objects.get(pk=pk)
    form = bicicletasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = bicicletas.objects.get(pk=pk)
    db.delete()
    return redirect('home')