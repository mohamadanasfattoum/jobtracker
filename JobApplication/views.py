from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from .models import JobApplication
from .forms import JobApplicationForm



class JobApplicationListView(generic.ListView):
    model = JobApplication
    context_object_name = "applications"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")
        search_query = self.request.GET.get("q")
        sort = self.request.GET.get("sort", "date_asc")


        if search_query:
            queryset = queryset.filter(
                Q(company_name__icontains=search_query)
                | Q(job_title__icontains=search_query)
                | Q(location__icontains=search_query)
            )

        if status:
            queryset = queryset.filter(status=status)

        if sort == "created_desc":
            queryset = queryset.order_by("-created_at")
        elif sort == "created_asc":
            queryset = queryset.order_by("created_at")
        elif sort == "date_desc":
            queryset = queryset.order_by("-application_date")
        else:
            queryset = queryset.order_by("application_date")

        return queryset


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["search_query"] = self.request.GET.get("q", "")
        context["selected_status"] = self.request.GET.get("status", "")
        context["selected_sort"] = self.request.GET.get("sort", "created_desc")

        
        context["total_count"] = JobApplication.objects.count()
        context["planned_count"] = JobApplication.objects.filter(status="planned").count()
        context["applied_count"] = JobApplication.objects.filter(status="applied").count()
        context["interview_count"] = JobApplication.objects.filter(status="interview").count()
        context["task_count"] = JobApplication.objects.filter(status="task").count()
        context["rejected_count"] = JobApplication.objects.filter(status="rejected").count()
        context["accepted_count"] = JobApplication.objects.filter(status="accepted").count()

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
