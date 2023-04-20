from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from flower.models import Flower

# Create your views here.
def flowers(request):
    flowers = Flower.objects.all()

    return render(request, 'flower/flower.html', {'flowers': flowers })

def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())
