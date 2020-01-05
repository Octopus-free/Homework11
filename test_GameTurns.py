from GameTurns import NextTurn
import unittest


class TestNextTurn:

    def test_turn_step(self):

        test_message = NextTurn()
        number = test_message.turn_number
        assert test_message.turn_step(number) == 'Ход 1'


class TestNextTurnWithUnittest(unittest.TestCase):

    def test_turn_step(self):
        test_message = NextTurn()
        number = test_message.turn_number
        self.assertEqual(test_message.turn_step(number), 'Ход 1')
        self.assertIsInstance(test_message.turn_step(number), str)
