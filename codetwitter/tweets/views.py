from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_timeline

# Create your views here.


def index(request):
    timeline = get_timeline()
    context = {'timeline': timeline}
    return render(request, 'tweets/index.html', context)
