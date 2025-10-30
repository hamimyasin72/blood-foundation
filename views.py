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



 
class DonorListView(ListView):
    model = Donor
    template_name = 'donor_list.html'
    context_object_name = 'donors'

class DonorDetailView(DetailView):
    model = Donor
    template_name = 'donor_detail.html'

class DonorCreateView(CreateView):
    model = Donor
    template_name = 'donor_form.html'
    fields = '__all__'
    success_url = reverse_lazy('donor_list')

class DonorUpdateView(UpdateView):
    model = Donor
    template_name = 'donor_form.html'
    fields = '__all__'
    success_url = reverse_lazy('donor_list')

class DonorDeleteView(DeleteView):
    model = Donor
    template_name = 'donor_confirm_delete.html'
    success_url = reverse_lazy('donor_list')
 
class DonationRequestListView(ListView):
    model = DonationRequest
    template_name = 'donationrequest_list.html'
    context_object_name = 'requests'

class DonationRequestDetailView(DetailView):
    model = DonationRequest
    template_name = 'donationrequest_detail.html'

class DonationRequestCreateView(CreateView):
    model = DonationRequest
    template_name = 'donationrequest_form.html'
    fields = '__all__'
    success_url = reverse_lazy('donationrequest_list')

class DonationRequestUpdateView(UpdateView):
    model = DonationRequest
    template_name = 'donationrequest_form.html'
    fields = '__all__'
    success_url = reverse_lazy('donationrequest_list')

class DonationRequestDeleteView(DeleteView):
    model = DonationRequest
    template_name = 'donationrequest_confirm_delete.html'
    success_url = reverse_lazy('donationrequest_list')


# ----------------- Hospital Views -----------------
class HospitalListView(ListView):
    model = Hospital
    template_name = 'hospital_list.html'
    context_object_name = 'hospitals'

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'hospital_detail.html'

class HospitalCreateView(CreateView):
    model = Hospital
    template_name = 'hospital_form.html'
    fields = '__all__'
    success_url = reverse_lazy('hospital_list')

class HospitalUpdateView(UpdateView):
    model = Hospital
    template_name = 'hospital_form.html'
    fields = '__all__'
    success_url = reverse_lazy('hospital_list')

class HospitalDeleteView(DeleteView):
    model = Hospital
    template_name = 'hospital_confirm_delete.html'
    success_url = reverse_lazy('hospital_list')


# ----------------- DonationHistory Views -----------------
class DonationHistoryListView(ListView):
    model = DonationHistory
    template_name = 'donationhistory_list.html'
    context_object_name = 'histories'

class DonationHistoryDetailView(DetailView):
    model = DonationHistory
    template_name = 'donationhistory_detail.html'

class DonationHistoryCreateView(CreateView):
    model = DonationHistory
    template_name = 'donationhistory_form.html'
    fields = '__all__'
    success_url = reverse_lazy('donationhistory_list')

class DonationHistoryUpdateView(UpdateView):
    model = DonationHistory
    template_name = 'donationhistory_form.html'
    fields = '__all__'
    success_url = reverse_lazy('donationhistory_list')

class DonationHistoryDeleteView(DeleteView):
    model = DonationHistory
    template_name = 'donationhistory_confirm_delete.html'
    success_url = reverse_lazy('donationhistory_list')
