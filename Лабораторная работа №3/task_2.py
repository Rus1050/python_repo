# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(first, second, devider=','):

    first = first.split(devider)
    second = second.split(devider)
    first = set(first)
    second = set(second)
    inter = first.intersection(second)
    print(inter)
    inter = list(inter)
    inter.sort()
    return inter


a = find_common_participants(participants_first_group, participants_second_group, '|')
print(a)
