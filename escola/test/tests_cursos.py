from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    
    def setUp(self):
        self.url = reverse('Cursos-list')
        self.user = User.objects.create_user(username='lais', password='lais')
        #FORÇAR AUTENTICAÇÃO
        self.client.force_authenticate(user=self.user)
        self.curso_01 = Curso.objects.create(
            codigo='CT01',descricao='Curso Teste 01',nivel='B'
        )
        self.curso_02 = Curso.objects.create(
            codigo='CT02',descricao='Curso Teste 02',nivel='I'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito, não se preocupe!')   

    # ## TESTANDO GET
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Test that first and second are equal. If the values do not compare equal, the test will fail.
        #self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    
    ## TESTANDO POST
    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        data = {
            'codigo':'CTT3',
            'descricao':'Curso teste 3',
            'nivel':'A'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #mostrar esses https no thunderclient

    ## TESTANDO DELETE - não permitir deletar como regra de negócio - adicionar http method no viewset
    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        #testar tirando o httpmethod do viewset
    
    # # TESTANDO PUT
    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'codigo':'CTT1',
            'descricao':'Curso teste 1 atualizado',
            'nivel':'I'
        }
        #data = self.curso_01
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)