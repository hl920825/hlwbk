from django.conf.urls import url

from blogs.views import index

urlpatterns = [
    url(r'^index/$',index,name="首页"),
]