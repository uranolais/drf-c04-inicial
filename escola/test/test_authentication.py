# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status

# class AuthenticationUserTestCase(APITestCase):

#     def setUp(self):
#         self.url = reverse('Estudantes-list')
#         self.user = User.objects.create_user('lais', password='lais')

#     def test_autenticacao_user_com_credenciais_corretas(self):
#         """Teste que verifica a autenticação de um user com as credenciais corretas"""
#         user = authenticate(username='lais', password='lais')
#         self.assertTrue((user is not None) and user.is_authenticated)

#      # CONFIRMAR QUE NÃO ESTÁ AUTENTICADO
#     def test_autenticacao_de_user_com_username_incorreto(self):
#         """Teste que verifica autenticação de um user com username incorreto"""
#         user = authenticate(username='las', password='lais')
#         self.assertFalse((user is not None) and user.is_authenticated)
    
#     def test_autenticacao_de_user_com_password_incorreto(self):
#         """Teste que verifica autenticação de um user com password incorreto"""
#         user = authenticate(username='lais', password='las')
#         self.assertFalse((user is not None) and user.is_authenticated)

#     def test_requisicao_get_nao_autorizada(self):
#         """Teste que verifica uma requisição GET não autorizada (sem autenticar)"""
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         # self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # fazer esse e puxar para o teste de estudante
#     def test_requisicao_get_com_user_autenticado(self):
#         """Teste que verifica uma requisição GET de um user autenticado"""
#         self.client.force_authenticate(self.user)
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


   

