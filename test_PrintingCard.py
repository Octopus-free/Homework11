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
        self.test_wrong_attribute = 'Класс не содержит атрибута test!'

    # создаем функцию для теста конструктора
    def test_init(self):
        self.assertEqual(self.test_human_number, self.print_card_one._human_number)
        self.assertEqual(self.test_human_card_one, self.print_card_one._human_card)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.print_card_one), self.test_human_message)

    # создаем функцию для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.print_card_one.print_human_card(), self.print_card_for_equal.print_human_card())

    # создаем функцию для теста __ne__
    def test__ne__(self):
        self.assertNotEqual(self.print_card_one.print_human_card(), self.print_card_two.print_human_card())

    # создаем функцию для теста __getattr__
    def test__getattr__(self):
        self.assertEqual(self.print_card_one.test, self.test_wrong_attribute)

    # функция для тестирования отрисовки карточек игроков людей
    def test_print_human_card(self):
        self.assertIn(self.test_human_card_one, self.print_card_one.print_human_card())


class TestPrintingComputersCard(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.cards_list_one = ['10', '11']
        self.cards_list_two = ['20', '21']
        self.card_one = '10'
        self.card_two = '11'
        self.print_list_one = PrintingComputersCard(self.cards_list_one)
        self.print_list_two = PrintingComputersCard(self.cards_list_two)
        self.cards_list_for_equal = PrintingComputersCard(self.cards_list_one)
        self.computer_message = 'Созданы 2 карточка(и) для компьютера(ов)'
        self.test_wrong_attribute = 'Класс не содержит атрибута test!'

    # создаем функцию для теста конструктора
    def test_init(self):
        self.assertEqual(self.cards_list_one, self.print_list_one._cards_list)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.print_list_one), self.computer_message)

    # создаем функцию для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.print_list_one.print_computers_cards(), self.cards_list_for_equal.print_computers_cards())

    # создаем функцию для теста __ne__
    def test__ne__(self):
        self.assertNotEqual(self.print_list_one.print_computers_cards(), self.print_list_two.print_computers_cards())

    # создаем функцию для теста __getattr__
    def test__getattr__(self):
        self.assertEqual(self.print_list_one.test, self.test_wrong_attribute)

    # функция для тестирования отрисовки карточек игроков людей
    def test_print_computers_cards(self):
        self.assertIn(self.card_one, self.print_list_one.print_computers_cards())
        self.assertIn(self.card_two, self.print_list_one.print_computers_cards())
        self.assertIn('Карточка компьютерного игрока 1 ', self.print_list_one.print_computers_cards())