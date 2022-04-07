from django import forms
from . models import Article

class ArticleForm(forms.ModelForm):
    # RADIO_SELECT = [
    #     (1,'1번'),
    #     (2,'2번'),
    #     (3,'3번'),
    # ]

    # title = forms.CharField(
    #     widget = forms.Textarea(
    #     attrs={
    #         'rows':'3'
    #         }
    #     ))
    # check_test_ssafy7 = forms.CharField(
    #     widget = forms.CheckboxInput(),
    #     required = False)
    # radio_test_ssafy7 = forms.CharField(
    #     widget = forms.RadioSelect(choices=RADIO_SELECT)
    # )
    class Meta:
        model = Article
        fields = '__all__'