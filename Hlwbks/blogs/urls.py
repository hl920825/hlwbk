from django.conf.urls import url

from blogs.views import index, detail, Register,Login,Comment,About,quits

urlpatterns = [
    url(r'^index/$', index, name="首页"),
    url(r'^detail/(?P<id>\d+)/$', detail, name="博客详情"),
    url(r'^register/$', Register.as_view(), name="注册"),
    url(r'^login/$', Login.as_view(), name="登录"),
    url(r'^about/$', About.as_view(), name="关于我"),
    url(r'^comment/$', Comment.as_view(), name="评论"),
    url(r'^quits/$',quits,name="注销"),
]
