import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.contrib.auth.models import Permission

def listar_permissoes():
    for permissao in Permission.objects.all():
        print(permissao.codename)

listar_permissoes()