from PlayersCondition import PlayersCondition
from unittest import mock
import unittest


class TestPlayerCondition(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.cards_list = PlayersCondition()
        self.players_count = 2
        self.test_list = [1, 2]

    def test_cards_for_human(self):

        # создаем лист, содержащий две карточки и сравниваем его с тестовым листом
        human_cards = self.cards_list.create_cards_for_human(self.players_count)
        self.assertEqual(len(human_cards), len(self.test_list))

    def test_cards_for_computers(self):

        # создаем лист, содержащий две карточки и сравниваем его с тестовым листом
        computers_cards = self.cards_list.create_cards_for_computers(self.players_count)
        self.assertEqual(len(computers_cards), len(self.test_list))

    def test_asking_players(self):

        # проверяем возможность функцию считывать из терминала
        with mock.patch('builtins.input', return_value=1):
            assert self.cards_list.asking_players() == [1, 1]
