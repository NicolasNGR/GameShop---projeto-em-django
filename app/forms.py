from django import forms
from app.models import Categoria, Contato, Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nome de usuário',
            'email': 'E-mail',
        }


class FormEditarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Nome de usuário',
            'email': 'E-mail',
        }


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {'nome': 'Nome da Categoria'}


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        labels = {
            'nome': 'Seu nome',
            'email': 'Seu e-mail',
            'assunto': 'Assunto',
            'mensagem': 'Mensagem',
        }


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'imagem', 'quantidade', 'preco', 'categoria']
        labels = {
            'nome': 'Nome do Jogo',
            'imagem': 'Imagem da Capa',
            'quantidade': 'Quantidade em Estoque',
            'preco': 'Preço (R$)',
            'categoria': 'Categoria',
        }
