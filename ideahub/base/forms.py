from django.forms import ModelForm
from .models import Panel


class PanelForm(ModelForm):
    class Meta:
        model = Panel
        fields = '__all__'
