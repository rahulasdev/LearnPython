from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from . import models
from . import serializers

class CommentsList(generics.ListAPIView):
    queryset=models.Comments.objects.all()
    serializer_class=serializers.CommentsSerializers


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Comments.objects.all()
    serializer_class=serializers.CommentsSerializers
