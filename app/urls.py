from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ─── Páginas Públicas ───
    path('quem-somos', views.quemSomos, name='quemsomos'),
    path('loja', views.loja, name='loja'),
    path('add-contato', views.addContato, name='addcontato'),

    # ─── Usuário ───
    path('cadastro', views.cadastrarUsuario, name='cadastro'),
    path('login', views.loginUsuario, name='login'),
    path('logout', views.logoutUsuario, name='logout'),
    path('editar-usuario', views.editarUsuario, name='editarusuario'),

    # ─── Categoria ───
    path('Categoria', views.listarCategoria, name='categoria'),
    path('del-categoria/<int:id_cat>', views.delCategoria, name='delcategoria'),
    path('add-categoria', views.addCategoria, name='addcategoria'),
    path('edit-categoria/<int:id_cat>', views.editCategoria, name='editcategoria'),

    # ─── Contato ───
    path('contato', views.listarContato, name='contato'),
    path('del-contato/<int:id_contato>', views.delContato, name='delcontato'),

    # ─── Produto ───
    path('produto', views.listarProduto, name='produto'),
    path('add-produto', views.addProduto, name='addproduto'),
    path('edit-produto/<int:id_prod>', views.editProduto, name='editproduto'),
    path('del-produto/<int:id_prod>', views.delProduto, name='delproduto'),

    # ─── Dashboard ───
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/usuarios', views.listarUsuarios, name='usuarios'),
    path('dashboard/usuarios/edit/<int:id_user>', views.editUsuarioAdmin, name='editusuarioadmin'),
    path('dashboard/usuarios/del/<int:id_user>', views.delUsuario, name='delusuario'),
]
