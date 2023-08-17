from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):

    finches = Finch.objects.all()
    #responding to the client, injecting the cats we found from the database into our cats/index.html template
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    #instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)
    

#these are attributes after the :
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'