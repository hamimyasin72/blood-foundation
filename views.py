from django.shortcuts import render, get_object_or_404
from .models import  Article, Member, CarouselSlide, NewsTicker
from collections import defaultdict

def home(request):
 
    articles = Article.objects.all()[:3]
    tickers = NewsTicker.objects.order_by('-created_at')[:10] 
    slides = CarouselSlide.objects.all()
    return render(request, "home.html", {
        'tickers': tickers,
        "articles": articles,
        "slides": slides
    })
def committee(request):
    return render(request, "committee.html")

def group(request):
    return render(request, "group.html")


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article_detail.html", {"article": article})




def members_list(request):
    members = Member.objects.all().order_by("district", "hospital", "name")
    return render(request, "members.html", {"members": members})





def membership_view(request):
    return render(request, "membership.html")


def education(request):
    return render(request, "education.html")


def faq(request):
    return render(request , "faq.html")