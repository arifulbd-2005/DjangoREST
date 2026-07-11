from rest_framework import serializers

class AiquestSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=25)
    course = serializers.CharField(max_length=20)
    course_description = serializers.IntegerField()
    seat = serializers.IntegerField()