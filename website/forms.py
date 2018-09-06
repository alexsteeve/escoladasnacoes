from helloworld.models import Estudante
from django import forms

# FORMULÁRIO DE INCLUSÃO DE ESTUDANTES
# -------------------------------------------

class InsereEstudanteForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Estudante

        # Campos que estarão no form
        fields = [
            'nome',
            'matricula',
            'email',
            'endereco',
            'cpf',
            'celular',
            'dataNascimento',
            'batismo',
            'escolaridade'
        ]
