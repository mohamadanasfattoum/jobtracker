from django.views import generic
from django.urls import reverse_lazy

from .models import JobApplication




class JobApplicationListView(generic.ListView):
    model = JobApplication
    context_object_name = "applications"


class JobApplicationCreateView(generic.CreateView):
    model = JobApplication
    fields = '__all__'
    success_url = reverse_lazy('application_list')
