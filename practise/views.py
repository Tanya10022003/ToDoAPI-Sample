from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import ToDoSerializer


# Create your views here.


class ToDoDetail(APIView):
    def get(self,request):
        obj=ToDo.objects.all()
        serializer=ToDoSerializer(obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ToDoInfo(APIView):
    def get(self, request,id):
        try:
            obj=ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            msg={"msg":"no error found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer=ToDoSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj=ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            msg={"msg":"no error found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer=ToDoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            obj=ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            msg={"msg":"no error found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer=ToDoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            obj=ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            msg={"msg":"no error found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg","delete successful"}, status=status.HTTP_204_NO_CONTENT)
    
        




          
