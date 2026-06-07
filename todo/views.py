from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views import View
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


class EditTaskView(UpdateView):
    model = Task
    fields = ["title"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('create-task')


class DoneTaskView(View):
    
    def post(self,request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        task.status = 'complete'
        task.save()
        return redirect('create-task')