from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MyCalendar
from .forms import MyCalendarForm

# Create your views here.

def index(request):
    return render(request, 'calendars/index.html')

def form(request):
    if request.method == 'POST':
        form = MyCalendarForm(request.POST)
        print form
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = MyCalendarForm()

    return render(request, 'form.html', {'form': form})