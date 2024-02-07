from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ListingForm


from .models import Listing


def home_view(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    listings_page = paginator.get_page(page)

    context = {
        'listings': listings_page
    }

    return render(request, 'listings/listing.html', context)


class listings_detail(DetailView):
    model = Listing
    template_name = 'listings/list_detail.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Listing, id=id)


class ListingCreate(LoginRequiredMixin, CreateView):
    form_class = ListingForm
    template_name = "listings/list_create.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, f"A new Listing has been approved")
        return "/listings/home/"




class update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ListingForm
    template_name = "listings/list_create.html"
    queryset = Listing.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Listing, id=id)


    def test_func(self):
        Listing = self.get_object()
        if Listing.realtor:
            return True
        else:
            return False

    def get_success_url(self):
        return "/listings/home/"

class delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    template_name = "listings/list_delete.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Listing, id=id)

    def test_func(self):
        Listing = self.get_object()
        if Listing.realtor:
            return True
        else:
            return False

    def get_success_url(self):
        return "/listings/home/"



