# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4
ensure_ascii = True


def task(filename) -> None:
    with open(filename, 'r') as file:
        list_ = []
        reader = csv.DictReader(file)
        for line_ in reader:
            list_.append(line_)

    with open(OUTPUT_FILENAME, 'w') as output_file:
        json.dump(list_, output_file, indent=indent, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    task(INPUT_FILENAME)
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
