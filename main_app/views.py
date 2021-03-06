from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches':finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all().values_list('id'))
    return render(request, 'finches/detail.html', {'finch' : finch, 'feeding_form':feeding_form, 'toys': toys_finch_doesnt_have})

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'color', 'favorite_music', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches_detail', finch_id=finch_id)

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys':toys})

def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys/detail.html', {'toy' : toy})

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finches_detail', finch_id=finch_id)

def remove_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('finches_detail', finch_id=finch_id)