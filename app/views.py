from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group, User
from app.models import Categoria, Contato, Produto
from app.forms import FormCategoria, FormContato, ProdutoForm, FormUsuario, FormEditarUsuario


# ─── Páginas Públicas ───

def index(request):
    produtos_destaque = Produto.objects.all()[:4]
    total_jogos = Produto.objects.count()
    total_categorias = Categoria.objects.count()
    return render(request, 'index.html', {
        'produtos_destaque': produtos_destaque,
        'total_jogos': total_jogos,
        'total_categorias': total_categorias,
    })


def quemSomos(request):
    usuarios = User.objects.all()[:3]
    return render(request, 'quem-somos.html', {'usuarios': usuarios})


def loja(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    if categoria_id:
        produtos = Produto.objects.filter(categoria_id=categoria_id)
        categoria_selecionada = int(categoria_id)
    else:
        produtos = Produto.objects.all()
        categoria_selecionada = None
    return render(request, 'loja.html', {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': categoria_selecionada,
    })


# ─── Usuário ───

def cadastrarUsuario(request):
    formulario = FormUsuario(request.POST or None)
    if request.method == 'POST':
        if formulario.is_valid():
            usuario = formulario.save()
            try:
                grupo_cliente = Group.objects.get(name='Cliente')
                usuario.groups.add(grupo_cliente)
            except Group.DoesNotExist:
                pass
            return redirect('login')
    return render(request, 'cadastro.html', {'form': formulario})


def loginUsuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')


def logoutUsuario(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editarUsuario(request):
    formulario = FormEditarUsuario(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request, 'edit-usuario.html', {'form': formulario})


# ─── Categoria ───

@login_required
@staff_member_required
def listarCategoria(request):
    _categorias = Categoria.objects.all().values()
    return render(request, 'categoria.html', {'categorias': _categorias})


@login_required
@staff_member_required
def delCategoria(request, id_cat):
    _categoria = get_object_or_404(Categoria, id=id_cat)
    _categoria.delete()
    return redirect('categoria')


@login_required
@staff_member_required
def addCategoria(request):
    formulario = FormCategoria(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')
    return render(request, 'add-categoria.html', {'form': formulario})


@login_required
@staff_member_required
def editCategoria(request, id_cat):
    _categoria = get_object_or_404(Categoria, id=id_cat)
    formulario = FormCategoria(request.POST or None, instance=_categoria)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')
    return render(request, 'edit-categoria.html', {'form': formulario})


# ─── Contato ───

@login_required
@staff_member_required
def listarContato(request):
    contatos = Contato.objects.all()
    return render(request, 'contato.html', {'contatos': contatos})


@login_required
@staff_member_required
def delContato(request, id_contato):
    _contato = get_object_or_404(Contato, id=id_contato)
    _contato.delete()
    return redirect('contato')


def addContato(request):
    formulario = FormContato(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request, 'add-contato.html', {'form': formulario})


# ─── Produto ───

@login_required
@staff_member_required
def listarProduto(request):
    _produtos = Produto.objects.all()
    return render(request, 'produto.html', {'produtos': _produtos})


@login_required
@staff_member_required
def addProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produto')
    else:
        form = ProdutoForm()
    return render(request, 'add-produto.html', {'form': form})


@login_required
@staff_member_required
def editProduto(request, id_prod):
    _produto = get_object_or_404(Produto, id=id_prod)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=_produto)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('produto')
    return render(request, 'edit-produto.html', {'form': form, 'produto': _produto})


@login_required
@staff_member_required
def delProduto(request, id_prod):
    _produto = get_object_or_404(Produto, id=id_prod)
    _produto.delete()
    return redirect('produto')


# ─── Dashboard ───

@login_required
@staff_member_required
def dashboard(request):
    total_produtos = Produto.objects.count()
    total_categorias = Categoria.objects.count()
    total_contatos = Contato.objects.count()
    total_usuarios = User.objects.count()
    return render(request, 'dashboard.html', {
        'total_produtos': total_produtos,
        'total_categorias': total_categorias,
        'total_contatos': total_contatos,
        'total_usuarios': total_usuarios,
    })


@login_required
@staff_member_required
def listarUsuarios(request):
    usuarios = User.objects.all().order_by('date_joined')
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@login_required
@staff_member_required
def editUsuarioAdmin(request, id_user):
    _usuario = get_object_or_404(User, id=id_user)
    formulario = FormEditarUsuario(request.POST or None, instance=_usuario)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios')
    return render(request, 'edit-usuario-admin.html', {'form': formulario, 'usuario': _usuario})


@login_required
@staff_member_required
def delUsuario(request, id_user):
    _usuario = get_object_or_404(User, id=id_user)
    _usuario.delete()
    return redirect('usuarios')
