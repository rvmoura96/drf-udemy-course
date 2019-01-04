from django.test import TestCase

from core.models import PontosTuristicos


# Models tests
class PontosTuristicosTest(TestCase):
    """Classe que manterá a suite de testes para o modelo PontosTuristicos."""

    def setUp(self):
        """Função de Setup para a suite dos testes."""
        self.ponto_turistico = PontosTuristicos.objects.create(
            nome='Bar do Zé',
            descricao='O famoso Bar do zézinho',
            aprovado=True
        )

    def test_criacao_ponto_turistico(self):
        """
        O atributo Ponto Turistico deve ser uma instancia de PontosTuristicos.

        O atributo pontos_turisticos deverá sera uma instancia do
        modelo PontosTuristicos.
        """
        self.assertTrue(isinstance(self.ponto_turistico, PontosTuristicos))

    def test_nome_ponto_turistico(self):
        """
        O retorno do método __str__ deve ser o nome da instancia.

        O valor retornado no método __str__ deverá ser o valor do atributo
        nome.
        """
        self.assertEqual(self.ponto_turistico.__str__(), 'Bar do Zé')
