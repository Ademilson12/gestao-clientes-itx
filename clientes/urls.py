from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete


urlpatterns = [
    path('list/', persons_list, name='person_list'), # Podemos colocar apelidos nas nossas urls
    path('new/', persons_new, name='person_new'),
    path('update/<int:id>/', persons_update, name='person_update'), # Já que precisamos saber o id do usuário que iremos alterar colocamos <int:id> na url
    path('delete/<int:id>/', persons_delete, name='person_delete'), # Já que precisamos saber o id do usuário que iremos excluir colocamos <int:id> na url
]