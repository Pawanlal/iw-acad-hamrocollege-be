from rest_framework import serializers

from .models import Announcement, Club, Member


class AnnouncementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'announce_by', 'message', 'created_at', 'modified_at', 'club']
        read_only_field = ['id']


class ClubModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'created_at']
        read_only_field = ['id']


class MemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'is_creator', 'club', 'user']
        read_only_field = ['id']

