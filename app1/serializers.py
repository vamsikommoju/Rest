from rest_framework import serializers
from app1.models import Course


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cname = serializers.CharField(max_length=40)
    dur = serializers.IntegerField()
    fee = serializers.IntegerField()

    def create(self,validateddata):
        return Course.objects.create(**validateddata)

    def update(self,instance,validateddata):
        instance.cname = validateddata.get('cname',instance.cname)
        instance.dur = validateddata.get('dur',instance.dur)
        instance.fee = validateddata.get('fee',instance.fee)
        instance.save()
        return instance