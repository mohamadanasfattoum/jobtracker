from django.urls import path
from .views import JobApplicationListView

urlpatterns = [
    path('', JobApplicationListView.as_view(), name="application_list"),
]