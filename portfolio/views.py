from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portfolio(request):
    Portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'Portfolios' : Portfolios})