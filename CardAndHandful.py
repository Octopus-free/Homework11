from random import sample


# класс для генерации мешка с бочонками
class HandfulGeneration:

    def __init__(self):
        self.handful = []

    # функция для заполнения мешка бочонками со значениями от 0 до 91
    def create(self):
        for number_from_handful in range(0, 91):
            self.handful.append(number_from_handful)
        return self.handful


class HandfulGame:

    def __init__(self):
        self.sack_for_game = HandfulGeneration().create()

    def handful_using(self):
        barrel = sample(self.sack_for_game, 1)[0]
        while barrel == ' ' or barrel == 0:
            barrel = sample(self.sack_for_game, 1)[0]
        self.sack_for_game[self.sack_for_game.index(barrel)] = ' '
        return barrel


class CardGeneration:

    def __init__(self):
        self.sack = HandfulGeneration().create()
        self.three_row_card = ''

    def create_card(self):

        for row_number in range(0, 3):

            card_row = []
            # рандомно выбираем бочонок из мешка для первой клетки карточки (значения от 1 до 9)
            # значение заменяем в мешке на ' ', для того чтобы не было дублей в других рядах одной и той же карточки
            choice_under_10 = sample(self.sack[0:10], 1)[0]
            while choice_under_10 == ' ' or choice_under_10 == 0:
                choice_under_10 = sample(self.sack[0:10], 1)[0]
            card_row.append(' {}'.format(choice_under_10))
            self.sack[self.sack.index(choice_under_10)] = ' '

            # рандомно заполняем остальные клетки на карточке (значения от 10 до 90)
            # значение заменяем в мешке на ' ', для того чтобы не было дублей в других рядах одной и той же карточки
            border_counter = 1
            for counter in range(1, 9):
                border_counter += 1
                choice = sample(self.sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(border_counter, '0'))], 1)[0]
                while choice == ' ':
                    choice = sample(self.sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(border_counter, '0'))], 1)[0]
                card_row.append(choice)
                self.sack[self.sack.index(choice)] = ' '

            # в каждой строке карточки рандомно зачищаем 4 клетки из 9
            for clear_position in range(1, 5):
                position_in_card_row = sample(card_row, 1)[0]
                while position_in_card_row == '  ':
                    position_in_card_row = sample(card_row, 1)[0]
                card_row[card_row.index(position_in_card_row)] = '  '

            for element in card_row:
                self.three_row_card += '{} '.format(str(element))
            self.three_row_card += '\n'

        return self.three_row_card[:-2]
