# from rest_framework.test import APITestCase
# from escola.models import Matricula, Estudante, Curso
# from django.urls import reverse
# from rest_framework import status

# class MatriculaTestCase(APITestCase):

#     def setUp(self):
#         self.url = reverse('Matriculas-list')
#         self.estudante = Estudante.objects.create(
#             nome='Estudante Teste',
#             email='estudante@gmail.com',
#             cpf='77567543010',
#             data_nascimento='2003-02-02',
#             celular='11 98765-4321'
#         )
#         self.curso = Curso.objects.create(
#             codigo='CTT',descricao='Curso Teste',nivel='B'
#         )
#         self.matricula = Matricula.objects.create(
#             estudante=self.estudante,
#             curso=self.curso,
#             periodo='M'
#         )

#     def test_requisicao_get_para_listar_matriculas(self):
#         """Teste para verificar a requisição GET para listar as matriculas"""
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK) #Test that first and second are equal. If the values do not compare equal, the test will fail.
#         #self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    
#     ## TESTANDO POST
#     def test_requisicao_post_para_criar_matricula(self):
#         """Teste para verificar a requisição POST para criar uma matrícula"""
#         data = {
#             'estudante': self.estudante.pk,
#             'curso': self.curso.pk,
#             'periodo': 'M'
#         }
#         response = self.client.post(self.url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         #mostrar esses https no thunderclient

#     ## TESTANDO DELETE - não permitir deletar como regra de negócio - adicionar http method no viewset
#     def test_requisicao_delete_para_deletar_matricula(self):
#         """Teste para verificar a requisição DELETE não permitida para deletar uma matrícula"""
#         response = self.client.delete('/matriculas/1/')
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
#     # # TESTANDO PUT
#     def test_requisicao_put_para_atualizar_matricula(self):
#         """Teste para verificar a requisição PUT não permitida para atualizar uma matricula"""
#         data = {
#             'estudante': self.estudante.pk,
#             'curso': self.curso.pk,
#             'periodo': 'V'
#         }
#         response = self.client.put('/matriculas/1/', data=data)
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)