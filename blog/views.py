from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
#위에서 .은 현재 디렉토리를 의미함

# Create your views here.
# view는 어플리케이션의 로직을 넣는 곳이다.
# 각 함수 하나하나를 각각 view라고 하는 듯. 
# urls.py에 있는 view의 이름과 일치해야 함. 근데 둘 중에 뭐랑 일치해야 하는거지?

def post_list(request):
    #QuerySet (: 전달받은 모델의 객체 목록)
    posts = Post.objects.all()
    #render 메소드 : request와 blog/post_list.html 템플릿을 받아 리턴!??
	#'posts'라는 이름에 posts 객체를 담아서 리턴
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	# 여기서의 "POST"는 http 메소드의 post임. 블로그 글 post와는 다름.
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			#대부분의 경우 commit=False를 쓰지 않고 바로 form.save()를 사용해서 저장
			#지금은 추가 정보를 입력해주어야 하므로 commit=False 사용.
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail',pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	
	return render(request, 'blog/post_edit.html', {'form': form})
