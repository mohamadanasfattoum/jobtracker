from django.urls import path
from .views import JobApplicationListView, JobApplicationCreateView, JobApplicationUpdateView, JobApplicationDeleteView, JobApplicationDetailView

urlpatterns = [
    path('', JobApplicationListView.as_view(), name="application_list"),
    path('<int:pk>/', JobApplicationDetailView.as_view(), name="application_detail"),    
    path('create/', JobApplicationCreateView.as_view(), name="application_create"),
    path('<int:pk>/update/', JobApplicationUpdateView.as_view(), name="application_update"),
    path('<int:pk>/delete/', JobApplicationDeleteView.as_view(), name="application_delete"),

]