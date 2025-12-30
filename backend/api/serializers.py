from rest_framework import serializers
from clubs.models import Club, Activity
from events.models import Event
from faculty.models import Faculty
from innovation.models import InnovationContribution


class ClubSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = ["id", "name", "description", "cover_image"]

    def get_cover_image(self, obj):
        return obj.cover_image.url if obj.cover_image else None


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "title", "description", "date"]


class EventSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    club = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "status", "club", "image"]

    def get_image(self, obj):
        return obj.image.url if obj.image else None


class FacultySerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ["id", "name", "designation", "department", "profile_image"]

    def get_profile_image(self, obj):
        return obj.profile_image.url if obj.profile_image else None


class InnovationSerializer(serializers.ModelSerializer):
    faculty = serializers.StringRelatedField()
    proof_image = serializers.SerializerMethodField()

    class Meta:
        model = InnovationContribution
        fields = ["id", "title", "description", "year", "faculty", "proof_image"]

    def get_proof_image(self, obj):
        return obj.proof_image.url if obj.proof_image else None
