from core.models import Availability
from core.tasks import notify_teacher_canceled_lesson
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import CreateLessonForm, JoinLessonForm


class AddAvailability(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Availability
    form_class = CreateLessonForm
    template_name = 'lessons/availability_form.html'
    success_url = reverse_lazy('core:home')
    permission_required = 'core.add'

    def form_invalid(self, form):
        messages.error(self.request, "This lesson already exists.")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Lesson added succesfuly.")
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ListAvailableLessons(LoginRequiredMixin, ListView):
    model = Availability
    template_name = 'lessons/list.html'
    context_object_name = 'lesson_list'

    def get_queryset(self):
        return Availability.objects.filter(is_booked=False)


class JoinLesson(UpdateView):
    model = Availability
    form_class = JoinLessonForm
    template_name = 'lessons/join.html'
    success_url = reverse_lazy('lessons:booked')

    def form_valid(self, form):
        form.instance.is_booked = True
        form.instance.student = self.request.user
        return super().form_valid(form)


class ListMyLessons(LoginRequiredMixin, ListView):
    model = Availability
    template_name = 'lessons/booked.html'
    context_object_name = 'lesson_list'

    def get_queryset(self):
        return Availability.objects.filter(Q(teacher=self.request.user) | Q(student=self.request.user))


class CancelLesson(UpdateView):
    model = Availability
    form_class = JoinLessonForm
    template_name = 'lessons/cancel.html'
    success_url = reverse_lazy('lessons:booked')

    def form_valid(self, form):
        form.instance.is_booked = False
        form.instance.student = None
        notify_teacher_canceled_lesson.delay(
            form.instance.date, form.instance.time, form.instance.teacher.email)
        return super().form_valid(form)
