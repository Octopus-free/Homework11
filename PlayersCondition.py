from CardAndHandful import CardGeneration


# создаем класс для запросов кол-ва игроков и формирования карточек для них
class PlayersCondition:

    # создаем фунцкцию для генерации карточек игроков (людей)
    def create_cards_for_human(self, players_count):
        # создаем пустой лист для дальнейшего хранения карточек играющих людей
        human_players_list = []
        for players in range(0, players_count):
            # инициализируем класс CardGeneration для создания карточки
            player_card_for_game = CardGeneration()
            player_card = player_card_for_game.create_card()
            # добавляем созданную карточку в лист
            human_players_list.append(player_card)
        return human_players_list

    # создаем фунцкцию для генерации карточек компьютерных игроков
    def create_cards_for_computers(self, computers_count):
        # создаем пустой лист для дальнейшего хранения карточек играющих компьютеров
        computers_players_list = []
        for players in range(0, computers_count):
            # инициализируем класс CardGeneration для создания карточки
            computer_card_for_game = CardGeneration()
            computer_card = computer_card_for_game.create_card()
            # добавляем созданную карточку в лист
            computers_players_list.append(computer_card)
        return computers_players_list

        # создаем функцию для запроса кол-ва игроков людей и компьютеров
    def asking_players(self):
        # создаем пустой лист для дальнейшего хранения кол-ва игроков
        players_list = []
        human_count = int(input('Сколько людей будет играть? '))
        computers_count = int(input('Сколько компьютеров будет играть? '))
        # добавляем в лист запрошенное в терминале кол-во игроков
        players_list.append(human_count)
        players_list.append(computers_count)
        return players_list



