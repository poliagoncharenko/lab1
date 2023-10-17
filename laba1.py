import csv
import random


with open ('books.csv', 'r') as f:
    f_csv = csv.reader(f, delimiter=";")
    num_long_titles = 0
    books = list(f_csv)
    books_after_2018 = []
    count_books = len(books)
    for book in books:
        if len(book[1]) > 30:
            num_long_titles += 1
    print(f'Количество записей {len(books) + 1}')
    print(f'Количество записей, у которых в поле Название строка длиннее 30 символов.{num_long_titles}')
    request = input('Введите автора ')
    for book in books:
        name = book[3]
        full_name = book[4]
        book_year = book[6].split('.')[-1][:4]
        years_range = [str(year) for year in range(2018, 2024)]
        if (request in [name, full_name]) and (book_year in years_range):
            books_after_2018.append(book)
    print(f'Книги {request} от 2018 года: {books_after_2018}')
    with open('generator.txt', 'w') as generator_books:
        for i in range(20):
            num = random.randint(0, len(books))
            author = books[num][3]
            generator_books.write(f'{num}){author}. {books[num][1]} - {books[num][6]}\n')
