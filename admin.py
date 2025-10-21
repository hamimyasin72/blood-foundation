from django.contrib import admin
from .models import  Article,Member, CarouselSlide
from .models import NewsTicker
admin.site.register(NewsTicker)



 

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "published_at")
    search_fields = ("title", "summary", "content")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital", "district", "city")
    search_fields = ("name", "hospital", "district", "city")
    list_filter = ("city", "district")

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


 