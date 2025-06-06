import csv
from datetime import date

class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        year, month, day = map(int, birth_date_str.split('-'))
        self.birth_date = date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"
    
    import csv

def modifier(filename):
    people = []

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        surname = row[0]
        first_name = row[1]
        birth_date = row[2]
        nickname = row[3] if len(row) > 3 and row[3] else None

        person = Person(surname, first_name, birth_date, nickname)
        fullname = person.get_fullname()
        age = person.get_age()

        row.insert(2, fullname) 
        row.append(age)        
        people.append(row)

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['surname', 'first_name', 'fullname', 'birth_date', 'nickname', 'age'])  # заголовки
        writer.writerows(people)


def modifier(filename):
    people = []

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        surname = row[0]
        first_name = row[1]
        birth_date = row[2]
        nickname = row[3] if len(row) > 3 and row[3] else None

        person = Person(surname, first_name, birth_date, nickname)
        fullname = person.get_fullname()
        age = person.get_age()

        row.insert(2, fullname) 
        row.append(age)        
        people.append(row)

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['surname', 'first_name', 'fullname', 'birth_date', 'nickname', 'age'])  # заголовки
        writer.writerows(people)