from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]
        
post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )

 
class PostListSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'user',
        ]


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]