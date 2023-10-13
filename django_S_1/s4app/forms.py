from django import forms


class ChoiceForm(forms.Form):
    games = forms.ChoiceField(choices=((1, "орел-решка"), (2, "кубики"), (3, "числа")))
    quant = forms.IntegerField(min_value=1, max_value=64,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))