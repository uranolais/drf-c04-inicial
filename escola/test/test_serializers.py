from django.test import TestCase
from escola.models import Estudante,Curso
from escola.serializers import EstudanteSerializer, CursoSerializer

class SerializersTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste Modelo',
            email='testemodelo@gmail.com',
            cpf='48373912061',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

        self.curso = Curso(
            codigo='CTM',descricao='Curso Teste Modelo',nivel='B'
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)
    
    def test_verifica_campos_serializados_estudante(self):
        """Teste que verifica os campos que estão sendo serializados do estudante"""
        data = self.serializer_estudante.data
        #mostrar os campos do serializer - testar tirando uma dessas opções
        self.assertEqual(set(data.keys()), set(['id','nome', 'email', 'cpf', 'data_nascimento','celular']))
    
    def test_verifica_conteudo_dos_campos_serializados_estudante(self):
        """Teste que verifica o conteudo dos campos serializados do estudante"""
        data = self.serializer_estudante.data
        self.assertEqual(data['nome'], self.estudante.nome)
        self.assertEqual(data['email'], self.estudante.email)
        self.assertEqual(data['cpf'], self.estudante.cpf)
        self.assertEqual(data['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(data['celular'], self.estudante.celular)

    def test_verifica_campos_serializados_curso(self):
        """Teste que verifica os campos que estão sendo serializados do curso"""
        data = self.serializer_curso.data
        self.assertEqual(set(data.keys()), set(['id','codigo', 'descricao', 'nivel']))
    
    def test_verifica_conteudo_dos_campos_serializados_curso(self):
        """Teste que verifica o conteudo dos campos serializados do curso"""
        data = self.serializer_curso.data
        self.assertEqual(data['codigo'], self.curso.codigo)
        self.assertEqual(data['descricao'], self.curso.descricao)
        self.assertEqual(data['nivel'], self.curso.nivel)
