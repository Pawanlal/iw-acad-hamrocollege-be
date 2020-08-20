from rest_framework import serializers
from .models import Attendance

class AttendanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'attendance_date', 'is_present', 'classroom', 'user', 'subject']
        read_only_fields = ['id']
