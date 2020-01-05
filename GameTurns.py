# создаем класса для генерации сообщения о ходе
class NextTurn:

    def __init__(self):
        self.turn_number = 1

    def turn_step(self, turn_number):

        turn_message = f'Ход {turn_number}'
        return turn_message

