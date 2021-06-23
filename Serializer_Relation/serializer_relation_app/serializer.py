from rest_framework import serializers
from .models import Singer, Song
# from .models import Student

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id','title','singer','duration']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True,slug_field='field')
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    song_serializer = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name','gender','song_serializer']


#for hyperlinked serializer
# class StudentSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Student
#         fields = ['id', 'url','name','roll','city']