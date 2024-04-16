from escola.models import Estudante, Curso
from django.test import TestCase

class ModelsTestCase(TestCase):
    # teste inicial
    # def test_falha(self):
    #     self.fail('Teste falhou')

    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste Modelo',
            email='testemodelo@gmail.com',
            cpf='48373912061',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso = Curso(
            codigo='CTM',descricao='Curso Teste Modelo',nivel='B'
        )

    def test_verifica_atributos_do_estudante(self):
        """Teste para verificar os atributos do modelo de estudante"""
        self.assertEqual(self.estudante.nome, 'Teste Modelo')
        self.assertEqual(self.estudante.email, 'testemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '48373912061')
        self.assertEqual(self.estudante.data_nascimento,'2003-02-02')
        self.assertEqual(self.estudante.celular, '86 99999-9999')
        #MUDAR OS ATRIBUTOS PARA TESTAR

    def test_verifica_atributos_do_curso(self):
        """Teste para verificar os atributos do modelo de curso"""
        self.assertEqual(self.curso.codigo, 'CTM')
        self.assertEqual(self.curso.descricao, 'Curso Teste Modelo')
        self.assertEqual(self.curso.nivel, 'B')

