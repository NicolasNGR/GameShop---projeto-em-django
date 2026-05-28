# 🎮 GameShop — Loja de Jogos Django

## Como rodar localmente

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

## Como publicar no PythonAnywhere (passo a passo)

### 1. Criar conta em pythonanywhere.com (plano gratuito serve)

### 2. No PythonAnywhere — abrir um Console Bash e rodar:

```bash
# Fazer upload do ZIP ou clonar
# Se fizer upload do ZIP pelo Files:
cd ~
unzip gameshop.zip
cd gameshop

# Instalar dependências
pip install --user -r requirements.txt

# Aplicar banco de dados
python manage.py migrate

# Criar admin
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic --noinput
```

### 3. Criar Web App

- Vá em **Web** > **Add a new web app**
- Escolha **Manual configuration**
- Escolha **Python 3.10**

### 4. Configurar WSGI

Clique em **WSGI configuration file** e substitua o conteúdo por:

```python
import os
import sys

path = '/home/SEU_USUARIO/gameshop'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'projeto.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Substitua `SEU_USUARIO` pelo seu nome de usuário do PythonAnywhere.**

### 5. Configurar arquivos estáticos

Em **Web > Static files**, adicione:

| URL         | Directory                                      |
|-------------|------------------------------------------------|
| `/static/`  | `/home/SEU_USUARIO/gameshop/staticfiles`       |
| `/media/`   | `/home/SEU_USUARIO/gameshop/media`             |

### 6. Atualizar ALLOWED_HOSTS

Em `projeto/settings.py`, edite a linha:
```python
ALLOWED_HOSTS = ['SEU_USUARIO.pythonanywhere.com']
```

### 7. Recarregar

Clique em **Reload** no painel Web. Pronto! 🎮

---

## Funcionalidades

- Página inicial com destaques
- Loja com filtro por categoria
- Cadastro e login de usuários
- Formulário de contato
- Dashboard administrativo (staff)
- CRUD completo: Jogos, Categorias, Contatos, Usuários
- Alteração de senha
