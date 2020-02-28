from django.shortcuts import render, redirect, get_object_or_404 # Redirect, função que o django tem, que faz o usuário retornar para uma url
#get_object_or_404 vai tentar recuperar o objeto que o usuário, caso não consiga retorna um 404 para mostrar que o recurso não existe
from .models import Person # importando Person da models 
from .forms import PersonForm # Agora importamos o form para que seja utilizado na view
from django.contrib.auth.decorators import login_required # Importando o login 


@login_required #Agora para acessar o usuário tem que estar logado
# Create your views here.
def persons_list(request):
    persons = Person.objects.all() # Por padrão o django nos fornece o object.all() para trazer as informações do banco
    #persons = Person.objects.get(id=) Podemos fazer um get e pegar pelo id
    return render(request, 'person.html', {"persons": persons})
    #Vamos usar o template que criamos, aproveitamos e passamos o person que vai receber os dados

@login_required
def persons_new(request): # agora vamos tratar 2 momento, 1:Enviar um form novo para pagina
    form = PersonForm(request.POST or None, request.FILES or None) # 1: Para quando o usuário estiver com dados preenchidos e fizer o post através do submit
    # Após a virgula, mandamos um None para caso o form esteja vazio
    if form.is_valid():# Se o form for valido
        form.save() # vamos salvar nosso form
        return redirect('person_list') # Faz retorna para url informada
    return render(request, 'person_form.html', {'form':form}) # 2: Agora precisamos entregar esse form para minha pagina
    # Após a virgula, estou enviando a variável form que eu criei acima para dentro do form

@login_required
def persons_update(request, id): # Recebe uma requisição e um id de usuário
    person = get_object_or_404(Person, pk=id) # Explicação do shortcut na linha 2, 'pk' é id de cada pessoa no banco
    form = PersonForm(request.POST or None, request.FILES or None, instance=person) # 'instace' retorna com o usuário que foi puxado no banco

    if form.is_valid(): # Condição para se o form for válido
        form.save()     # Salva informações do form
        return redirect('person_list') # Retorna para lista de usuários

    return render(request, 'person_form.html', {'form':form}) # Caso não seja valido ele retorna o form normal

@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'form': form})