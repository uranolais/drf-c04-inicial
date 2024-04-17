from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
from escola.serializers import CursoSerializer

class CursoTestCase(APITestCase):
    
    fixtures = ['prototipo_banco.json']

    def setUp(self):
        self.url = reverse('Cursos-list')
        #tem que mudar as credenciais pq agr ta batendo com os dados do fixtures
        self.user = User.objects.create_user(username='admin', password='admin')
        # #FORÇAR AUTENTICAÇÃO
        # self.client.force_authenticate(user=self.user)
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
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Test that first and second are equal. If the values do not compare equal, the test will fail.
        #self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    # ## TESTANDO GET 01 CURSO
    def test_requisicao_get_para_um_curso(self):
        """Teste para verificar a requisição GET para listar um cursos"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data,dados_curso_serializados)

    ## TESTANDO POST
    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        self.client.force_authenticate(user=self.user)
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
        self.client.force_authenticate(user=self.user)
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        #testar tirando o httpmethod do viewset
    
    # # TESTANDO PUT
    def test_requisicao_put_para_atualizar_curso(self):
        self.client.force_authenticate(user=self.user)
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'codigo':'CTT1',
            'descricao':'Curso teste 1 atualizado',
            'nivel':'I'
        }
        #data = self.curso_01
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)