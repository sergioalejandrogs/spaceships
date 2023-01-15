from django.shortcuts import render, redirect
from .models import Ship
from .forms import ShipForm

# Create your views here.

def index(request):
    ships = Ship.objects.all()
    return render(request, 'pages/index.html', {'ships': ships})

def add(request):
    form = ShipForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'pages/add.html', {'form': form})

def edit(request, id):
    ship = Ship.objects.get(id=id)
    form = ShipForm(request.POST or None, request.FILES or None, instance=ship)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('index')
    return render(request, 'pages/edit.html', {'form': form})

def delete(request, id):
    ship = Ship.objects.get(id=id)
    ship.delete()
    return redirect('index')
