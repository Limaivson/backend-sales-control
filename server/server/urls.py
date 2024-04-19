from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inserir-funcionario/', inserir_funcionario, name='inserir_funcionario'),
    path('listar-funcionarios/', listar_funcionarios, name='listar_funcionarios'),
    path('deletar-funcionario/', deletar_funcionario, name='deletar_funcionario'),
    path('atualizar-funcionario/', atualizar_funcionario, name='atualizar_funcionario'),
    path('buscar-funcionario/', buscar_funcionario, name='buscar_funcionario'),
    path('buscar-funcionario-nome/', buscar_funcionario_por_nome, name='buscar_funcionario_por_nome'),
    path('listar-clientes/', listar_clientes, name='listar_clientes'),
    path('listar-clientes-pagos/', listar_clientes_pagos, name='listar_clientes_pagos'),
    path('inserir-cliente/', inserir_cliente, name='inserir_cliente'),
    path('deletar-cliente/', deletar_cliente, name='deletar_cliente'),
    path('atualizar-cliente/', atualizar_cliente, name='atualizar_cliente'),
    path('buscar-cliente/', buscar_cliente, name='buscar_cliente'),
    path('buscar-cliente-nome/', buscar_cliente_por_nome, name='buscar_cliente_por_nome'),
    path('buscar-cliente-endereco/', buscar_cliente_por_endereco, name='buscar_cliente_por_endereco'),
    path('listar-pagamentos/', listar_pagamentos, name='listar_pagamentos'),
    path('inserir-pagamento/', inserir_pagamento, name='inserir_pagamento'),
    path('deletar-pagamento/', deletar_pagamento, name='deletar_pagamento'),
    path('atualizar-pagamento/', atualizar_pagamento, name='atualizar_pagamento'),
    path('buscar-pagamento/', buscar_pagamento, name='buscar_pagamento'),
]
