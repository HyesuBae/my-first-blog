from django.conf.urls import url
from . import views

urlpatterns = [
    # post_list라는 이름의 view가 ^$ URL에 할당됨.
    # name='post_list'는 URL에 이름 붙인 것으로 뷰를 식별한다.
    #뷰의 이름과 같을 수도 다를 수도 있다.
    url(r'^$', views.post_list, name='post_list'),
]
