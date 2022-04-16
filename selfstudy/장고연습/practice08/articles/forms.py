from .models import Article,Comment
from django import forms
from dataclasses import field

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):

    PICKS = [
        ('red','RED'),
        ('blue','BLUE')
    ]
    pick = forms.CharField(
        widget= forms.Select(choices=PICKS)
    )

    class Meta:
        model = Comment
        fields = ('pick','content',)