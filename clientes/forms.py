from django.forms import ModelForm # Importamos a o forms django
from .models import Person # Model que importamos para ser utilizado na subclasse meta


class PersonForm(ModelForm): # Criamos uma classe PersonForm que herda de ModelForm
    class Meta: # Definimos uma subclasse 'Meta' como mostra a documentação para definir o model que queremos usar
        model = Person # É a model da minha ModelForm
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']# Quais campos que terão a minha model 

