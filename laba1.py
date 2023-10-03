import csv
import random


with open ('books.csv', 'r') as f:
    f_csv = csv.reader(f, delimiter=";")
    count30 = 0
    books = []
    bookss = []
    c = 0
    for x in f_csv:
        c += 1
        if c > 1:
            books.append(x)
    for x in books:
        if len(x[1]) > 30:
            count30 += 1
    print('Количество записей', len(books) + 1)
    print('Количество записей, у которых в поле Название строка длиннее 30 символов.', count30)
    request = input('Введите автора ')
    for x in books:
        if (x[3] == request or x[4] == request) and ('2018' in x[6] or '2019' in x[6] or '2020' in x[6] or '2021' in x[6] or '2022' in x[6] or '2023' in x[6]):
            bookss.append(x)
    print(f'Книги {request} от 2018 года: {bookss}')
    with open('generator.txt', 'w') as g:
        for i in range(20):
            num = random.randint(0, len(books))
            g.write(f'{num}){books[num][3]}. {books[num][1]} - {books[num][6]}\n')