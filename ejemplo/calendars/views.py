from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MyCalendar
from .forms import MyCalendarForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView

# Create your views here.

def index(request):
    return render(request, 'calendars/index.html')

class CalendarCreateForm(CreateView):
    template_name = 'form.html'
    model = MyCalendar
    fields = '__all__'
    #form_class = MyCalendarForm
    success_url = '/create/thanks/'

    def form_valid(self, form):
        form.save()
        return super(CalendarCreateForm, self).form_valid(form)

calendar_create = CalendarCreateForm.as_view()

class CalendarDetailView(DetailView):
    model = MyCalendar

    def get_context_data(self, **kwargs):
        context = super(CalendarDetailView, self).get_context_data(**kwargs)
        return context

calendar_detail = CalendarDetailView.as_view()

class CalendarDelete(DeleteView):
    model = MyCalendar
    template_name = "calendars/calendar_delete.html"
    success_url = reverse_lazy('calendar_delete_confirm')
    def get_object(self, queryset=None):
        obj = super(CalendarDelete, self).get_object()
        return obj

calendar_delete = CalendarDelete.as_view()

class DeleteConfirm(TemplateView):
    template_name = "delete_confirm.html"

delete_confirm = DeleteConfirm.as_view()

class CalendarEdit(UpdateView):
    model = MyCalendar
    template_name = "form.html"
    succes_url = reverse_lazy('calendar_edit_confirm')
    fields = '__all__'
    def get_object(self, queryset=None):
        obj = super(CalendarEdit, self).get_object()
        return obj

calendar_edit = CalendarEdit.as_view()

class EditConfirm(TemplateView):
    template_name = "edit_confirm.html"

edit_confirm = EditConfirm.as_view()

class CalendarList(ListView):
    model = MyCalendar

    def get_context_data(self, **kwargs):
        context = super(CalendarList, self).get_context_data(**kwargs)
        return context

calendar_list = CalendarList.as_view()
