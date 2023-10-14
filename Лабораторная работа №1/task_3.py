# TODO Найдите количество книг, которое можно разместить на дискете
memory_of_disk = 1.44
mb = 1024
kb = 1024
symbols = 25
strings = 50
pages = 100
memory_per_symbol = 4
memory = memory_of_disk * mb * kb #Перевод информационного объёма дискеты в байты
memory_of_single_book = memory_per_symbol * symbols * strings * pages
number_of_books = memory // memory_of_single_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
