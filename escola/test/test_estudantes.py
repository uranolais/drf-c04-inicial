from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from escola.models import Estudante
from django.urls import reverse
from rest_framework import status

class EstudanteTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('Estudantes-list')
        self.user = User.objects.create_user(username='lais', password='lais')
        #FORÇAR AUTENTICAÇÃO
        self.client.force_authenticate(user=self.user)
        self.estudante_01 = Estudante.objects.create(
            nome='Estudante Teste UM',
            email='et1@gmail.com',
            cpf='43151764002',
            data_nascimento='2003-02-02',
            celular='11 98765-4321'
        )
        self.estudante_02 = Estudante.objects.create(
            nome='Estudante Teste DOIS',
            email='et2@gmail.com',
            cpf='87115124078',
            data_nascimento='2003-02-02',
            celular='11 98765-4322'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito, não se preocupe!') 

    ## TESTANDO GET
    def test_requisicao_get_para_listar_estudantes(self):
        """Teste para verificar a requisição GET para listar os estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Test that first and second are equal. If the values do not compare equal, the test will fail.
        #self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    ## TESTANDO POST
    def test_requisicao_post_para_criar_estudante(self):
        """Teste para verificar a requisição POST para criar um estudante"""
        data = {
            'nome':'Teste',
            'email':'et3@gmail.com',
            'cpf':'00061443069',
            'data_nascimento':'2003-02-02',
            'celular':'66 95984-7070'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #mostrar esses https no thunderclient

    # ## TESTANDO DELETE - não permitir deletar como regra de negócio - adicionar http method no viewset
    def test_requisicao_delete_para_deletar_estudante(self):
        """Teste para verificar a requisição DELETE permitida para deletar um curso"""
        response = self.client.delete('/estudantes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #testar tirando o httpmethod do viewset
    
    # # # TESTANDO PUT
    def test_requisicao_put_para_atualizar_estudante(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'nome':'Teste',
            'email':'et3@gmail.com',
            'cpf':'00061443069',
            'data_nascimento':'2003-02-02',
            'celular':'66 95984-7070'
        }
        response = self.client.put('/estudantes/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)