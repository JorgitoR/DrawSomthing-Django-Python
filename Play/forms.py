from django import forms
from .models import solucion


class FormularioSolucion(forms.ModelForm):

	class Meta:
		model = solucion
		fields = [
			"length",
			"letras"
		]