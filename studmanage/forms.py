from django.forms import ModelForm
from .models import StudData


class form(ModelForm):
    class Meta:
        model=StudData
        fields= "__all__"
