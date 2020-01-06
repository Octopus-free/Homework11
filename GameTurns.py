# создаем класса для генерации сообщения о ходе
class NextTurn:

    def __init__(self):
        self.turn_number = 1

    # переопределяем метод __str__
    def __str__(self):
        return 'Класс для генерации ходов'

    # переопределяем метод __eq__
    def __eq__(self, other):
        return self.turn_number == other.turn_number

    # переопределяем метод __ne__
    def __ne__(self, other):
        return self.turn_step() != other.turn_step()

    def turn_step(self, turn_number):

        turn_message = f'Ход {turn_number}'
        return turn_message

