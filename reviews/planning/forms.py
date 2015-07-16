from django import forms

from reviews.models import Keyword


class KeywordForm(forms.ModelForm):
    description = forms.CharField(
            widget=forms.TextInput(attrs={ 'class': 'form-control' }),
            max_length=200,
            required=True
        )
    related_to = forms.ChoiceField(
            widget=forms.Select(attrs={ 'class': 'form-control' }, choices=Keyword.RELATED_TO),
            required=False
        )

    class Meta:
        model = Keyword
        fields = ['description', 'related_to', ]

class SynonymForm(KeywordForm):
    class Meta:
        model = Keyword
        fields = ['description', 'related_to', 'synonym_of',]
