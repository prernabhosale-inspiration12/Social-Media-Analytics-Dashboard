from django import forms


class PredictionForm(forms.Form):

    likes = forms.IntegerField(
        label="Likes"
    )

    comments = forms.IntegerField(
        label="Comments"
    )

    shares = forms.IntegerField(
        label="Shares"
    )