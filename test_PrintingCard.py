from PrintingCard import PrintingHumanCard, PrintingComputersCard
import unittest


class TestHumanCard(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.print_card_one = PrintingHumanCard(1, '10')
        self.print_card_two = PrintingHumanCard(2, '20')
        self.print_card_for_equal = PrintingHumanCard(1, '10')
        self.test_human_number = 1
        self.test_human_card_one = '10'
        self.test_human_card_two = '20'
        self.test_human_message = 'Создана 1 карточка для 1-го игрока'

    # создаем функцию для теста конструктора
    def test_init(self):
        self.assertEqual(self.test_human_number, self.print_card_one._human_number)
        self.assertEqual(self.test_human_card_one, self.print_card_one._human_card)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.print_card_one), self.test_human_message)

    # создаем карточку для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.print_card_one.print_human_card(), self.print_card_for_equal.print_human_card())

    # создаем карточку для теста __ne__
    def test__ne__(self):
        self.assertNotEqual(self.print_card_one.print_human_card(), self.print_card_two.print_human_card())

    # функция для тестирования отрисовки карточек игроков людей
    def test_print_human_card(self):
        self.assertIn(self.test_human_card_one, self.print_card_one.print_human_card())
