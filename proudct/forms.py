from django import forms
from .models import ProudctReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model=ProudctReview
        fields=['rate','review']