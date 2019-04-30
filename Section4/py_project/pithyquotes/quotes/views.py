from django.shortcuts import render
from quotes.models import Quote
# Create your views here.

def index(request):
    return render(request, 'index.html')

def quotes(request):
    data = Quote.objects.all()
    context ={
            'data': data}
    return render(request, 'quotes.html', context)
