from django.forms import ModelForm, TextInput

from image.models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': TextInput(attrs={'size': 2})
        }
