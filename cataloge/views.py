from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def index(request):
    num_book = models.Book.objects.all().count()
    num_author = models.Author.objects.all().count()
    num_book_instance = models.BookInstance.objects.all().count()
    num_book_instance_available = models.BookInstance.objects.filter(status__exact='a').count()
    context = {
        'num_book': num_book,
        'num_author': num_author,
        'num_book_instance': num_book_instance,
        'num_book_instance_available': num_book_instance_available,
    }
    return render(request, 'index.html', context)   

class BookCreate(LoginRequiredMixin,generic.CreateView): 
    model = models.Book
    fields = '__all__'  
    success_url = '/cataloge'  
    template_name = 'create.html'

class Register(generic.CreateView): 
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/register.html'


class BookDetail(generic.DetailView):
    model = models.Book
    template_name = 'detail.html'
    context_object_name = 'book'
    success_url = reverse_lazy('cataloge')