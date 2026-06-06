from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class AddTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title']


    def get_success_url(self):
        return self.request.get_full_path()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(user=self.request.user)
        return context
    


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('create-task') # نام URL صفحه لیست تسک‌ها را اینجا بنویسید

    def get_queryset(self):
        # فقط اجازه می‌دهد کاربر تسک‌های خودش را حذف کند
        return self.model.objects.filter(user=self.request.user)