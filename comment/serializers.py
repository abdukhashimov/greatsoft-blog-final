from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField)
from comment.models import Comment


class CommentSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = SerializerMethodField()
    created_at = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'replies', 'created_at')

    def get_user(self, obj):
        output = {}
        output['email'] = str(obj.user)
        output['profile_picture'] = obj.user.get_profile_picture
        return output

    def get_replies(self, obj):
        comments = obj.child_comments
        reply = []
        comment_dict = {}
        for comment in comments:
            comment_dict['user'] = str(comment.user)
            comment_dict['reply'] = {
                'text': comment.comment,
                'created_at': str(comment.created_at),
                'parent_id': str(comment.parent_id)
            }
            reply.append(comment_dict.copy())
        return reply

    def get_created_at(self, obj):
        return str(obj.created_at)
