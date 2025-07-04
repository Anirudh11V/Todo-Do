from django.forms import ModelForm
from .models import todotask


class taskForm(ModelForm):
    class Meta:
        model = todotask
        fields = '__all__'