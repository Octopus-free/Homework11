# создаем класс для отрисовки в терминале карточек игроков
class PrintingHumanCard:

    # создаем конструктор для экзепляра класса
    def __init__(self, human_number, human_card):
        self._human_number = human_number
        self._human_card = human_card

    # переопределяем метод __str__
    def __str__(self):
        return f'Создана 1 карточка для {self._human_number}-го игрока'

    # переопределяем метод __eq__
    def __eq__(self, other):
        return self.print_human_card() == other.print_human_card()

    # переопределяем метод __ne__
    def __ne__(self, other):
        return self.print_human_card() != other.print_human_card()

    # функция для отрисовки карточек игроков людей
    def print_human_card(self):

        name_message = f'Карточка игрока {self._human_number} '
        underline_message = f'--'*13
        func_message = f'{name_message}\n{underline_message}\n{self._human_card}\n{underline_message}'
        return func_message


class PrintingComputersCard:

    # создаем конструктор для экзепляра класса
    def __init__(self, cards_list):
        self._cards_list = cards_list

    # переопределяем метод __str__
    def __str__(self):
        return f'Созданы {len(self._cards_list)} карточка(и) для компьютера(ов)'

    # переопределяем метод __eq__
    def __eq__(self, other):
        return self.print_computers_cards() == other.print_computers_cards()

    # переопределяем метод __ne__
    def __ne__(self, other):
        return self.print_computers_cards() != other.print_computers_cards()

    # функция для отрисовки карточек игроков компьютеров
    def print_computers_cards(self):

        func_message = ''
        for computer_card in self._cards_list:
            computer_number = self._cards_list.index(computer_card) + 1
            name_message = f'Карточка компьютерного игрока {computer_number} '
            underline_message = f'--' * 13
            func_message += f'{name_message}\n{underline_message}\n{computer_card}\n{underline_message}\n'
        return func_message
