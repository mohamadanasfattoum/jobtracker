from django.views import generic
from django.urls import reverse_lazy

from .models import JobApplication
from .forms import JobApplicationForm



class JobApplicationListView(generic.ListView):
    model = JobApplication
    context_object_name = "applications"
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")

        if status:
            queryset = queryset.filter(status=status)

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_status"] = self.request.GET.get("status", "")
        return context

class JobApplicationCreateView(generic.CreateView):
    model = JobApplication
    form_class = JobApplicationForm  # statt fields="__all__", damit wir die Formularfelder kontrollieren können
    success_url = reverse_lazy('application_list')


class JobApplicationUpdateView(generic.UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = "JobApplication/jobapplication_form.html"
    success_url = reverse_lazy('application_list')


class JobApplicationDeleteView(generic.DeleteView):
    model = JobApplication
    template_name = "JobApplication/jobapplication_confirm_delete.html"
    success_url = reverse_lazy('application_list')
