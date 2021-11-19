from django import forms
from .models import Post, CommunityComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'community_img')

class CommunityCommentForm(forms.ModelForm):
    class Meta:
        model = CommunityComment
        fields = ('content',)
