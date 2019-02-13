from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    mainBody = models.TextField(verbose_name="正文")
    main_digest = models.TextField(verbose_name="摘要",null=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    status_choices = (
        ("d","不发表"),
        ("p","发表"),
    )
    status = models.CharField(max_length=1,choices=status_choices,default="p",verbose_name="文章状态")
    liulans = models.PositiveIntegerField(default=0,verbose_name="浏览量")
    comment = models.PositiveIntegerField(default=0,verbose_name="评论量")
    article_order = models.IntegerField(blank=False,null=False,default=0,verbose_name="排序")
    category = models.ForeignKey(to="Category",verbose_name="分类",blank=False,null=False)
    tags = models.ManyToManyField(to="Tag",verbose_name="标签")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time','-article_order']
        verbose_name = "文章"
        verbose_name_plural = verbose_name



# 分类  存储文章的分类信息
class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="类名")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time = models.DateTimeField(auto_now=True,verbose_name="修改时间")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

# 标签
class Tag(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    change_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    name = models.CharField(max_length=30,verbose_name="标签名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

# 评论
class Comments(models.Model):
    content = models.CharField(max_length=250,verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加评论时间")
    change_time = models.DateTimeField(auto_now=True,verbose_name="修改评论时间")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除")
    article = models.ForeignKey(to="blogs.Article",verbose_name="所属文章")

    class Meta:
        verbose_name = "评论管理"
        verbose_name_plural = verbose_name

# 用户
class User(models.Model):
    phone = models.CharField(max_length=11,
                             verbose_name='手机号',
                             validators=[
                                 RegexValidator(r'^1[3-9]\d{9}$', "手机号码格式错误!")
                             ])
    password = models.CharField(max_length=32, verbose_name='密码')
    integral = models.SmallIntegerField(verbose_name='积分', default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone


















