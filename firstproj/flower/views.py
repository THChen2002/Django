from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from flower.models import Flower
from .forms import FlowerForm

# Create your views here.
def flowers(request):
    flowers = Flower.objects.all()

    return render(request, 'flower/flower.html', {'flowers': flowers })

def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())

def create(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/flower/')
    else:
        form = FlowerForm()
    return render(request, 'flower/edit.html', {'form': form})

def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = FlowerForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('flower/')
    else:
        form = FlowerForm(instance=flower)

    return render(request, 'flower/edit.html', {'form': form})

def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    return render(request, 'flower/')