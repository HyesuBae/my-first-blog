from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
#위에서 .은 현재 디렉토리를 의미함

# Create your views here.
# view는 어플리케이션의 로직을 넣는 곳이다.
# 각 함수 하나하나를 각각 view라고 하는 듯. 

def post_list(request):
    #QuerySet (: 전달받은 모델의 객체 목록)
    posts = Post.objects.all()
    #render 메소드 : request와 blog/post_list.html 템플릿을 받아 리턴!??
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
