from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from blogs.forms import UserForm, LoginForm
from blogs.helper import set_password, json_msg
from blogs.models import Article, Category, User, Tag, Comments


# 首页
def index(request):
    if request.method == "GET":
        # 未删除的所有文章
        articles = Article.objects.filter(is_delete=False)
        # 未删除的标签
        tags = Tag.objects.filter(is_delete=False)
        # Paginator 实现分页
        paginator = Paginator(articles,10)
        # 获取当前页面的页码
        page = request.GET.get('page',1)
        # 获取当前页码的数据
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # 页码不是整数 显示第一页
            articles = paginator.page(1)
        except EmptyPage:
            # 页码为空 显示最后一页
            articles = paginator.page(paginator.num_pages)

        context = {
            "articles":articles,
            "tags":tags,
        }
        return render(request,"blogs/index.html",context=context)

# 详情
def detail(request,id):
    if request.method == "GET":
        # 当前文章信息
        article = Article.objects.get(pk=id)
        # 浏览量加1
        article.liulans += 1
        article.save()
        # 获取文章对应评论
        comments = article.comments_set.all()
        context = {
            "article":article,
            "comments":comments,
        }
        return render(request,"blogs/detail.html",context=context)
    else:
        # 接受参数
        content = request.POST.get("content")
        # 保存到数据库
        article = Article.objects.get(pk=id)
        # 评论加1
        article.comment += 1
        article.save()
        Comments.objects.create(content=content,article=article)
        return JsonResponse(json_msg(0,"评论成功!"))


# 注册
class Register(View):
    def get(self,request):
        return render(request,"blogs/register.html")

    def post(self,request):
        # 接收参数
        data = request.POST
        # 验证数据合法性
        form = UserForm(data)
        if form.is_valid():
            # 保存到数据库
            user = User()
            user.phone = form.cleaned_data.get('phone')
            user.password = set_password(form.cleaned_data.get("password"))
            user.save()
            return redirect("blogs:登录")
        else:
            return render(request,"blogs/register.html",context=form.errors)


# 登录
class Login(View):
    def get(self, request):
        return render(request, "blogs/login.html")

    def post(self, request):
        # 接收参数
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            # 合法
            user = form.cleaned_data["user"]
            request.session["ID"] = user.pk
            request.session["phone"] = user.phone
            # 跳转到首页
            return redirect("blogs:首页")
        else:
            return render(request,"blogs/login.html",context=form.errors)

# 留言
class Comment(View):
    def get(self, request):
        return render(request, "blogs/comment.html")

    def post(self, request):
        pass

# 关于我们
class About(View):
    def get(self, request):
        return render(request, "blogs/aboutUs.html")

    def post(self, request):
        pass

def quits(request):
    if request.method == "GET":
        request.session.flush()
        return redirect("blogs:登录")