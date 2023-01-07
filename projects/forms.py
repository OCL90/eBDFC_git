from django.forms import ModelForm
from .models import Bol, Pad, Stage, Well, sandType

class BolForm(ModelForm):
    class Meta:
        model = Bol
        fields = '__all__'

class PadForm(ModelForm):
    class Meta:
        model = Pad
        exclude = ['job_id']

class SandTypeForm(ModelForm):
    class Meta:
        model = sandType
        exclude = ['slug']

class WellForm(ModelForm):
    class Meta:
        model = Well
        fields = '__all__'

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'