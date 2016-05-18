from django.conf.urls import url
from . import views

urlpatterns = [
    # post_list라는 이름의 view가 ^$ URL에 할당됨.
    # name='post_list'는 URL에 이름 붙인 것으로 뷰를 식별한다.
    # 뷰의 이름과 같을 수도 다를 수도 있다.
    url(r'^$', views.post_list, name='post_list'),
	# (?P<pk>[0-9]+): 여기에 넣은 모든 것을 pk 변수에 넣어 view로 전송한다는 뜻.
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/new/$', views.post_new, name='post_new'),
]
