from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MyCalendar
from .forms import MyCalendarForm
from django.views.generic.edit import FormView, CreateView

# Create your views here.

def index(request):
    return render(request, 'calendars/index.html')

class CalendarCreateForm(CreateView):
    template_name = 'form.html'
    model = MyCalendar
    fields = '__all__'
    #form_class = MyCalendarForm
    success_url = '/thanks/'

    def form_valid(self, form):
        #form.send_email()
        return super(CalendarCreateForm, self).form_valid(form)

calendar_create = CalendarCreateForm.as_view()