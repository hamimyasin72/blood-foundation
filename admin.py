from django.contrib import admin
from .models import  Article,Member, CarouselSlide
from .models import NewsTicker
 
from .models import RareBloodDonor
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

 

@admin.register(RareBloodDonor)
class RareBloodDonorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'blood_group',
        'location',
        'availability',
        'last_donated',
        'added_on',
    )
    list_filter = (
        'blood_group',
        'availability',
        'gender',
        'location',
    )
    search_fields = (
        'name',
        'phone',
        'email',
        'location',
        'blood_group',
    )
    ordering = ('blood_group', 'name')
    list_editable = ('availability', 'last_donated')
    readonly_fields = ('added_on',)
    list_per_page = 25
    fieldsets = (
        ("Personal Information", {
            'fields': ('name', 'age', 'gender')
        }),
        ("Blood Details", {
            'fields': ('blood_group', 'custom_blood_type', 'last_donated', 'availability')
        }),
        ("Contact Information", {
            'fields': ('phone', 'email', 'location')
        }),
        ("System Info", {
            'fields': ('added_on',),
            'classes': ('collapse',)
        }),
    )

 
 
