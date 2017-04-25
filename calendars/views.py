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
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'calendar/index.html')

class CalendarCreateForm(CreateView):
    template_name = 'calendar/form.html'
    model = MyCalendar
    fields = '__all__'
    #form_class = MyCalendarForm
    success_url = '/calendar/create/done/'

    def form_valid(self, form):
        form.save()
        return super(CalendarCreateForm, self).form_valid(form)

calendar_create = CalendarCreateForm.as_view()

class CreateConfirm(TemplateView):
    template_name = "calendar/create_confirm.html"

create_confirm = CreateConfirm.as_view()

class CreateUserForm(CreateView):
    template_name = 'calendar/form_create_user.html'
    model = User
    fields = ('username', 'email', 'password')
    #form_class = UserForm
    success_url = '/calendar/createuser/done/'

    def form_valid(self, form):
        form.save()
        new_user = User.objects.create_user(**form.cleaned_data)
        login(new_user)
        return super(CreateUserForm, self).form_valid(form)

create_user = CreateUserForm.as_view()

class CreateUserConfirm(TemplateView):
    template_name = "calendar/create_user_confirm.html"

create_user_confirm = CreateConfirm.as_view()

class CalendarDetailView(DetailView):
    model = MyCalendar
    template_name = "calendar/mycalendar_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CalendarDetailView, self).get_context_data(**kwargs)
        return context

calendar_detail = CalendarDetailView.as_view()

class CalendarDelete(DeleteView):
    model = MyCalendar
    template_name = "calendar/calendar_delete.html"
    success_url = reverse_lazy('calendar_delete_confirm')
    def get_object(self, queryset=None):
        obj = super(CalendarDelete, self).get_object()
        return obj

calendar_delete = CalendarDelete.as_view()

class DeleteConfirm(TemplateView):
    template_name = "calendar/delete_confirm.html"

delete_confirm = DeleteConfirm.as_view()

class CalendarEdit(UpdateView):
    model = MyCalendar
    template_name = "calendar/form.html"
    succes_url = reverse_lazy('calendar_create_confirm')
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
    template_name = "calendar/mycalendar_list.html"
    def get_context_data(self, **kwargs):
        context = super(CalendarList, self).get_context_data(**kwargs)
        return context

calendar_list = CalendarList.as_view()
