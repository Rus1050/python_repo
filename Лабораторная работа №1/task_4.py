users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_unique = set(users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visits = {"Общее количество": len(users),"Уникальные посещения": len(users_unique)}
print(visits)