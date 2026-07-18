from django.urls import path
from .views import JobApplicationListView, JobApplicationCreateView, JobApplicationUpdateView

urlpatterns = [
    path('', JobApplicationListView.as_view(), name="application_list"),
    path('create/', JobApplicationCreateView.as_view(), name="application_create"),
    path('<int:pk>/update/', JobApplicationUpdateView.as_view(), name="application_update"),
]