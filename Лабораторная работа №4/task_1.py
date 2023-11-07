# TODO решите задачу
import json


name_of_file = "input.json"


def task(filename: str) -> float:
    with open(filename) as file:
        data = json.load(file)
        summa = round(sum([numbers["score"]*numbers["weight"] for numbers in data]), 3)
        return summa


print(task(name_of_file))
