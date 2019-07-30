from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    # 블로그 모든 글들을 대상으로 
    blog_list = Blog.objects.all()
    # 블로그 객체 3 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지 알아내고 
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs , 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력한 내용을 DB에 넣는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 블로그 객체에 가져온 값을 저장 
    return redirect('/blog/' + str(blog.id)) # 완료 후에 해당 url로 이동

def blogpost(request, blog_id=None):
    blog = Blog()
    if blog_id:
        blog = get_object_or_404(Blog, pk=blog_id)
    
    form = BlogPost(request.POST or None, instance=blog)
    # 사용자가 입력한 내용을 처리하는 기능 -> POST
    if request.method=='POST'and form.is_valid():
        # form = BlogPost(request.POST) # 입력된 값들을 BlogPost모델 형식으로 받아옴
        post = form.save(commit = False)
        post.pub_date=timezone.now()
        post.save()
        return redirect('/')

    # 빈 페이지를 띄워주는 기능 -> GET
    #else:
    #    form = BlogPost()
    #    return render(request, 'new.html', {'form' : form})
    return render(request, 'new.html', {'form' : form}) # 새로운 일정 추가

# 일정을 삭제하는 함수
def delete(request, blog_id=None): 
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()

    return redirect('/')
