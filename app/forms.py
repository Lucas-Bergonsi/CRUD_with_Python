from django.forms import ModelForm
from app.models import bicicletas

# Create the form class.
class bicicletasForm(ModelForm):
     class Meta:
        model = bicicletas
        fields = ['marca', 'modelo', 'tamanho', 'ano']


