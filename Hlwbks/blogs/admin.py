from django.contrib import admin

# Register your models here.

from blogs.models import Article,Tag,Category

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","title","mainBody","change_time","status","liulans","category"]
    list_display_links = ["id","title","mainBody"]

