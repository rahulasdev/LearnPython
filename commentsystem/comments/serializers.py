from rest_framework import serializers
from . import models

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        fields =('id','content','created_at','updated_at')
        model=models.Comments
