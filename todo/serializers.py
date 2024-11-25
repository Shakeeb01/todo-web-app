from rest_framework import serializers
from .models import todoitem

class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoitem
        fields = ['id','title','description','is_completed','due_date']