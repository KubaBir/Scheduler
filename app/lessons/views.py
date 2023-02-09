from core.models import Availability
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LessonForm


class AddAvailability(LoginRequiredMixin, CreateView):
    model = Availability
    form_class = LessonForm
    template_name = 'lessons/availability_form.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
