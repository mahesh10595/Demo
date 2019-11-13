from django.forms import forms
from app1.models import MarchantModel,ProductModel


class MarchantForm(forms.ModelForm):
	class Meta:
		models = MarchantModel
		fields = ['email','password']

class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductModel
		fields = "__all__"