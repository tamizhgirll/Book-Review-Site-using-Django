from django import forms
from app1.models import Recommend

class RecommendForm(forms.ModelForm):
    class Meta:
        model = Recommend
        fields =  "__all__"