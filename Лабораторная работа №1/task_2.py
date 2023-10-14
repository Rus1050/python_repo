list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

half_number_of_players = len(list_players)//2
team_1 = list_players[:half_number_of_players]
team_2 = list_players[half_number_of_players:]
print(team_1)
print(team_2)