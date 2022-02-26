from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        labels = {'user_name': 'Your name', 'review_text': 'Your feedback', 'rating': 'Your rating'}
        error_messages = {'user_name': {'required': 'Please enter your name!'}}
