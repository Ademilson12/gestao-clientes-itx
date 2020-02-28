from django.contrib import admin
from django.urls import path, include # Importamos o include
from clientes import urls as clientes_urls # Importamos as urls de clientes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # Import para utilizar login e logout personalizado do django
from home import urls as home_urls # Importando o arquivo que está dentro de home/urls.py

urlpatterns = [    
    path('', include(home_urls)), # Descrição acima
    path('login/', auth_views.LoginView.as_view(), name='login'), # Importa view de login do Django
    path('clientes/',include(clientes_urls)), # Utilizamos o apontamento de clientes
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
