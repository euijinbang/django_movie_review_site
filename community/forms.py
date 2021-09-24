from django.forms import ModelForm
from community.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'