from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_01 = Curso.objects.create(
            codigo='CT01',descricao='Curso Teste 01',nivel='B'
        )
        self.curso_02 = Curso.objects.create(
            codigo='CT02',descricao='Curso Teste 02',nivel='I'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito, não se preocupe!')   

    
