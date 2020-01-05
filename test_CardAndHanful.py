from CardAndHandful import CardGeneration
from CardAndHandful import HandfulGame
from CardAndHandful import HandfulGeneration
import unittest


class TestHandfulGeneration(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_handful = HandfulGeneration()

    # функция для теста конструктора
    def test_init_handful_generation(self):
        handful = self.test_handful.handful
        self.assertEqual(len(handful), 0)

    # функция для теста наполнения мешка бочонками
    def test_create_handful(self):
        full_handful = self.test_handful.create()
        self.assertEqual(len(full_handful), 91)


class TestHandfulGame(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_sack = HandfulGame()

    # функция для теста конструктора
    def test_init_handful_game(self):
        sack = self.test_sack.sack_for_game
        self.assertEqual(len(sack), 91)

    # функция для теста вытаскивания из мешка бочонка
    def test_handful_using(self):
        self.assertIsInstance(self.test_sack.handful_using(), int)


class TestCardGeneration(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_card = CardGeneration().three_row_card
        self.create_card = CardGeneration().create_card()
        self.test_sack = HandfulGeneration().create()

    # функция для теста конструктора
    def test_init_card_generation(self):
        self.assertEqual(self.test_card, '')
        self.assertEqual(len(self.test_sack), 91)

    # создаем функцию для тестирования процесса создания карточки
    def test_create_card(self):
        self.assertIsInstance(self.test_card, str)
        self.assertIn(' ', self.create_card)

