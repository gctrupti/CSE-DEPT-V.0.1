from rest_framework.generics import ListAPIView
from clubs.models import Club
from events.models import Event
from faculty.models import Faculty
from innovation.models import InnovationContribution

from .serializers import (
    ClubSerializer,
    EventSerializer,
    FacultySerializer,
    InnovationSerializer,
)


class ClubListView(ListAPIView):
    queryset = Club.objects.filter(is_active=True)
    serializer_class = ClubSerializer


class EventListView(ListAPIView):
    queryset = Event.objects.all().order_by("-date")
    serializer_class = EventSerializer


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.filter(is_active=True)
    serializer_class = FacultySerializer


class InnovationListView(ListAPIView):
    queryset = InnovationContribution.objects.all().order_by("-year")
    serializer_class = InnovationSerializer
