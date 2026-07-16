from django.urls import path
from .views import JobApplicationListView, JobApplicationCreateView

urlpatterns = [
    path('', JobApplicationListView.as_view(), name="application_list"),
    path('create/', JobApplicationCreateView.as_view(), name="application_create"),
]