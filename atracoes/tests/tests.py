from django.test import TestCase

from atracoes.models import Atracao
from core.models import PontosTuristicos


class AtracoesTest(TestCase):
    """Classe que manterá a suite de testes para o modelo Atracao."""

    def setUp(self):
        """Função de setup para os testes."""
        ponto_turistico = PontosTuristicos.objects.create(
            nome='Bar do Zé',
            descricao='O famoso Bar do zézinho',
            aprovado=True
        )

        self.atracao = Atracao.objects.create(
            nome='Alien Brain',
            descricao='Drink de Alien Brain',
            horario='00:00',
            idade_minima=16,
            ponto_turistico=ponto_turistico
        )

    def test_criacao_de_atracao(self):
        """
        O atributo atracao deverá ser uma instancia de Atracao.

        O Atributo atracao deverá ser uma instancia do modelo
        Atracao.
        """
        self.assertTrue(isinstance(self.atracao, Atracao))

    def test_nome_da_atracao(self):
        """
        O retorno do método __str__ deverá ser o nome da instancia.

        O valor retornado no método __str__ deverá ser o valor do atributo
        nome.
        """
        self.assertEqual(self.atracao.__str__(), 'Alien Brain')
