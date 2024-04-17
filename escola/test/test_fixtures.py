from django.test import TestCase
from escola.models import Estudante, Curso
# python manage.py dumpdata > prototipo_banco.json

class FixtureDataTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_verifica_carregamento_da_fixture(self):
        estudante = Estudante.objects.get(cpf = '65748106809')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.cpf, '65748106809')
        self.assertEqual(curso.codigo,'CPOO1')