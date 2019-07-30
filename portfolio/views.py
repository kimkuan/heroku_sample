from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio
from .form import Post
from django.core.files.storage import FileSystemStorage # 파일저장

# Create your views here.

def portfolio(request):
    Portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'Portfolios' : Portfolios})

def newpost(request):
    return render(request, 'newpost.html')

def post(request, post_id=None): # post 생성 및 수정

    portfolio = Portfolio()
    if post_id:
        portfolio = get_object_or_404(Portfolio, pk=post_id)
    
    form = Post(request.POST or None, request.FILES, instance=portfolio)  
   
    if request.method=='POST'and form.is_valid():
        post = form.save(commit = False)
        post.save()
        # messages.success(request, "Thank you! You have successfully posted your picture!")
        return redirect('portfolio')

    return render(request, 'newpost.html', {'form' : form}) # 새로운 일정 추가


def post_delete(request, post_id=None): # post 삭제
    post = get_object_or_404(Portfolio, pk=post_id)
    post.delete()
    return redirect('portfolio')
