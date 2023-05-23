from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def counter(request):
    wordcounter1=request.POST.get("text")
    amount=len((wordcounter1).replace(',','').split())
    return render(request, 'counter.html', {'amount':amount})