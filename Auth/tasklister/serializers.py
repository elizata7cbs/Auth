from tasklister.models import Task, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password':{'write_only':True}}
        fields = ['id','username','email','is_admin','date_joined']


class TaskSerializer(serializers.ModelSerializer):
    user=UserSerializer(required=False)
    class Meta:
        model = Task
        fields = '__all__'



