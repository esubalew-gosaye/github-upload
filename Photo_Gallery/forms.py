from .models import*
from django.forms import ModelForm


class AddForm(ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


