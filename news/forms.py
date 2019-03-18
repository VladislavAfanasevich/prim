from django.forms import ModelForm
from news.models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
