from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import todoitem
from .serializers import TodoitemSerializer



class AllTodos(APIView):
    def get(self,request):
        queryset = todoitem.objects.all()
        serializer = TodoitemSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TodoitemSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    
    

class TodoDetail(APIView):
    def get(self,request,id):
        todo = get_object_or_404(todoitem,pk=id)
        serializer = TodoitemSerializer(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,id):
        todo = get_object_or_404(todoitem,pk=id)
        serializer = TodoitemSerializer(todo,data = request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        todo = get_object_or_404(todoitem,pk=id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        