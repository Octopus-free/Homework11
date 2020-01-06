from GameTurns import NextTurn
import unittest


class TestNextTurnWithUnittest(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.test_turn = NextTurn()
        self.test_turn_for_eq = NextTurn()
        self.test_turn_number = 1
        self.test_message = 'Класс для генерации ходов'

    # создаем функцию для теста конструктора
    def test_init(self):
        self.assertEqual(self.test_turn.turn_number, self.test_turn_number)

    # создаем функцию для теста __str__
    def test__str__(self):
        self.assertEqual(str(self.test_turn), self.test_message)

    # создаем функцию для теста __eq__
    def test__eq__(self):
        self.assertEqual(self.test_turn.turn_number, self.test_turn_for_eq.turn_number)

    # создаем функцию для теста __ne__
    def test__ne__(self):
        self.assertNotEqual(self.test_turn.turn_step(1), self.test_turn_for_eq.turn_step(2))

    # создаем функцию для теста вывода сообщения о текущем ходе
    def test_turn_step(self):
        test_message = NextTurn()
        number = test_message.turn_number
        self.assertEqual(test_message.turn_step(number), 'Ход 1')
        self.assertIsInstance(test_message.turn_step(number), str)
