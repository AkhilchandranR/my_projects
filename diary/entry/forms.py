from django.forms import ModelForm
from .models import entry
class EntryForm(ModelForm):
	class Meta:
		model=entry
		fields="__all__"