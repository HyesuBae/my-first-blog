from django.shortcuts import render

# Create your views here.
# view는 어플리케이션의 로직을 넣는 곳이다.

def post_list(request):
    #render 메소드 : request와 blog/post_list.html 템플릿을 받아 리턴!??
    return render(request, 'blog/post_list.html', {})
