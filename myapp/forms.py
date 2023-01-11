from django import forms

class AddLabelForm(forms.Form):
    label = forms.CharField(max_length = 200)

class AddFeatureForm(forms.Form):
    feature = forms.CharField(max_length=200)