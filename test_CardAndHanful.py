from CardAndHandful import CardGeneration
from CardAndHandful import HandfulGame
from CardAndHandful import HandfulGeneration
import unittest


class TestHandfulGeneration(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_handful_one = HandfulGeneration()
        self.test_handful_two = HandfulGeneration()
        self.test_handful_for_not_eq = []
        self.test_message = 'Создан пустой мешок для бочонков'

    # функция для теста конструктора
    def test_init_handful_generation(self):
        handful = self.test_handful_one.handful
        self.assertEqual(len(handful), 0)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.test_handful_one), self.test_message)

    # создаем функцию для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.test_handful_one.create(), self.test_handful_two.create())

    # создаем функцию для теста __ne__
    def test__ne__(self):
        for element in range(1, 92):
            self.test_handful_for_not_eq.append(element)
        self.assertNotEqual(self.test_handful_one.create(), self.test_handful_for_not_eq)

    # функция для теста наполнения мешка бочонками
    def test_create_handful(self):
        full_handful = self.test_handful_one.create()
        self.assertEqual(len(full_handful), 91)


class TestHandfulGame(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_sack_one = HandfulGame()
        self.test_sack_two = HandfulGame()
        self.test_message = 'Мешок для бочонков наполнен!'

    # функция для теста конструктора
    def test_init_handful_game(self):
        sack = self.test_sack_one.sack_for_game
        self.assertEqual(len(sack), 91)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.test_sack_one), self.test_message)

    # создаем функцию для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.test_sack_one, self.test_sack_two)

    # создаем функцию для теста __ne__
    def test__ne__(self):
        while self.test_sack_one.handful_using() == self.test_sack_two.handful_using():
            self.assertNotEqual(self.test_sack_one.handful_using(), self.test_sack_two.handful_using())

    # функция для теста вытаскивания из мешка бочонка
    def test_handful_using(self):
        self.assertIsInstance(self.test_sack_one.handful_using(), int)


class TestCardGeneration(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_card = CardGeneration()
        self.test_card_for_eq = CardGeneration()
        self.create_card = CardGeneration().create_card()
        self.test_sack = HandfulGeneration()
        self.test_sack_for_eq = HandfulGeneration()
        self.test_message = 'Мешок для бочонков наполнен, можно наполнять карточки'

    # функция для теста конструктора
    def test_init_card_generation(self):
        self.assertEqual(self.test_card.three_row_card, '')
        self.assertEqual(len(self.test_sack.create()), 91)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.test_card), self.test_message)

    # создаем функцию для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.test_sack, self.test_sack_for_eq)

    # создаем функцию для теста __ne__
    def test__ne__(self):
        self.assertNotEqual(self.test_card.create_card(), self.test_card_for_eq.create_card())

    # создаем функцию для тестирования процесса создания карточки
    def test_create_card(self):
        self.assertIsInstance(self.test_card.create_card(), str)
        self.assertIn(' ', self.create_card)

