from django.urls import path
from .views import (
    ClubListView,
    EventListView,
    FacultyListView,
    InnovationListView,
)

urlpatterns = [
    path("clubs/", ClubListView.as_view()),
    path("events/", EventListView.as_view()),
    path("faculty/", FacultyListView.as_view()),
    path("innovation/", InnovationListView.as_view()),
]
