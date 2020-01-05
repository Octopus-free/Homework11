from CheckingCard import CheckingCard
import unittest


# класс для тестирования функций в классе CheckingCard
class TestCheck(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.card = CheckingCard()
        self.zero_card = ['--', '--']
        self.full_card = [' 8 ', '11']
        self.full_card_over10 = [' 10', '11']
        self.full_card_after_strike_under10 = [' - ', '11']
        self.full_card_after_strike = [' --', '11']
        self.card_under10 = ' 8 11'
        self.strike_card_under10 = ' - 11'
        self.card10 = ' 10 11'
        self.strike_card = ' -- 11'
        self.wrong_card_under10 = ' 5 11'
        self.wrong_card10 = ' 11 12'
        self.human_win_message = 'Игрок 1 победил!'
        self.computer_win_message = 'Компьютер 1 победил!'
        self.human_lose_message = 'Игрок 1 проиграл, выпавшего бочонка нет на вашей карточке!'
        self.computer_lose_message = 'Компьютер 1 проиграл, выпавшего бочонка нет на вашей карточке!'
        self.strike_lose_message = 'Игрок 1 проиграл, необходимо было зачеркнуть число, выпавшее на бочонке!'
        self.barrel_number_under10 = 8
        self.barrel_number = 10

    def test_human_card_for_win(self):

        # сравниваем пустую карточку с выигрышным сообщением для игрока 1 человека
        self.assertEqual(self.card.check_human_players(self.zero_card), self.human_win_message)

    def test_computer_card_for_win(self):

        # сравниваем пустую карточку с выигрышным сообщением для игрока 1 компьютера
        self.assertEqual(self.card.check_computer_players(self.zero_card), self.computer_win_message)

    def test_answer_yes(self):

        # подаем на вход функции (ответ 'да' на вопрос 'зачеркнуть') бочонок №8 и карточку, содержащую число 8
        # проверяем, что функция 'зачеркивает' число
        card_for_strike_under10 = self.card.strike_numbers_answer_yes(1, self.barrel_number_under10, self.card_under10)
        self.assertEqual(card_for_strike_under10, self.strike_card_under10)

        # подаем на вход функции (ответ 'да' на вопрос 'зачеркнуть') бочонок №10 и карточку, содержащую число 10
        # проверяем, что функция 'зачеркивает' число
        card_for_strike = self.card.strike_numbers_answer_yes(1, self.barrel_number, self.card10)
        self.assertEqual(card_for_strike, self.strike_card)

        # подаем на вход функции (ответ 'да' на вопрос 'зачеркнуть') бочонок №8 и карточку, не содержащую число 8
        # проверяем, что функция выводит сообщение об ошибочном зачеркивании
        wrong_card_under10 = self.card.strike_numbers_answer_yes(1, self.barrel_number_under10, self.wrong_card_under10)
        self.assertEqual(wrong_card_under10, self.human_lose_message)

        # подаем на вход функции (ответ 'да' на вопрос 'зачеркнуть') бочонок №10 и карточку, не содержащую число 10
        # проверяем, что функция выводит сообщение об ошибочном зачеркивании
        wrong_card = self.card.strike_numbers_answer_yes(1, self.barrel_number, self.wrong_card10)
        self.assertEqual( wrong_card, self.human_lose_message)

    def test_answer_no(self):

        # подаем на вход функции (ответ 'нет' на вопрос 'зачеркнуть') бочонок №8 и карточку, содержащую число 8
        # проверяем, что функция 'зачеркивает' число
        card_not_strike = self.card.strike_numbers_answer_no(1, self.barrel_number_under10, self.card_under10)
        self.assertEqual(card_not_strike, self.strike_lose_message)

        # подаем на вход функции (ответ 'нет' на вопрос 'зачеркнуть') бочонок №10 и карточку, содержащую число 10
        # проверяем, что функция 'зачеркивает' число
        card_not_strike = self.card.strike_numbers_answer_no(1, self.barrel_number, self.card10)
        self.assertEqual(card_not_strike, self.strike_lose_message)

    def test_strike_computers_cards(self):

        # подаем на вход функции бочонок №8  и список карточек игроков компьютеров
        # для проверки автоматического зачеркивания числа на карточках
        cards_strike_under10 = self.card.strike_numbers_for_computers(self.barrel_number_under10, self.full_card)
        self.assertEqual(cards_strike_under10, self.full_card_after_strike_under10)

        # подаем на вход функции бочонок №10  и список карточек игроков компьютеров
        # для проверки автоматического зачеркивания числа на карточках
        cards_strike = self.card.strike_numbers_for_computers(self.barrel_number, self.full_card_over10)
        self.assertEqual(cards_strike, self.full_card_after_strike)



