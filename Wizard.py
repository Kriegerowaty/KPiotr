import json
import re
import sys
import pandas as pd

users = []


def add_user():
    n = 0
    next_user = 'y'
    while next_user in ['y', 'ye', 'yes']:
        name = input('\nEnter your name: ')
        surname = input('Enter your surname: ')
        city = input('Enter your address (city): ')#sdfs
        post_code = input('Enter your address (post code): ')
        street = input('Enter your address (street): ')
        home_number = input('Enter your address (number): ')
        address = city + ' ' + post_code + ' ' + street + ' ' + home_number
        phone = input('Enter your phone: ')
        salary = int(input('Enter what salary are you expecting: '))
        users.append(User(name, surname, city, post_code, street, home_number, address, phone, salary))
        User.change_data(users[n])
        next_user = input('Do you want to add next user? (y/n): ')
        n = n + 1


def add_user_param():
    try:
        name = sys.argv[1]
        surname = sys.argv[2]
        city = sys.argv[3]
        post_code = sys.argv[4]
        street = sys.argv[5]
        home_number = sys.argv[6]
        # address = sys.argv[7]
        phone = sys.argv[7]
        salary = int(sys.argv[8])
        address = city.capitalize() + ' ' + post_code + ' ' + street.capitalize() + ' ' + home_number
        users.append(User(name, surname, city, post_code, street,
                          home_number, address, phone, salary))
        User.multi_validate(users[0])
    except IndexError:
        print('Wrong parameteres')
        add_user()


def print_all():
    return [User.print_data(i) for i in users]


def save_to_json():
    with open('data.json', 'w') as json_file:
        for user in users:
            json.dump(User.organize_data(user), json_file, indent=6)
        # json.dump(User.organize_data(users[1]), json_file)
        # json.dump(str(User.organize_data(users[1])), json_file)


def save_to_excel():
    df_json = pd.read_json('data.json')
    print(df_json)
    # df_json.to_excel('data.xlsx')


class User:

    def __init__(self, name: str, surname: str,
                 city: str, post_code: str, street: str, home_number: str, address: str,
                 phone: str, salary: int):
        self.name = name
        self.validate_name()

        self.surname = surname
        self.validate_surname()

        self.city = city
        self.post_code = post_code
        self.street = street
        self.home_number = home_number

        self.address = address
        self.validate_address()

        self.phone = phone
        self.validate_phone()

        self.salary = salary
        self.validate_salary()

    def full_address(self):
        self.address = self.city.capitalize() + ' ' + self.post_code \
                       + ' ' + self.street.capitalize() + ' ' + self.home_number

    def validate_name(self):
        while not (self.name.isalpha() and 2 < len(self.name) < 15 and ' ' not in self.name):
            print('Wrong data format')
            self.name = input('Enter your name: ')

    def validate_surname(self):
        while not (all(x.isalpha() or x.isspace() for x in self.surname) and 2 < len(self.surname) < 30):
            print('Wrong data format')
            self.surname = input('Enter your surname: ')
            
    # def is_valid_post_code(self):
    #     post_code_separated = self.post_code.split('-')
    #     is_correct_formatting = True if post_code_separated[0].isdecimal() and len(post_code_separated[0]) == 2 \
    #                                     and
    #                                     post_code_separated[1].isdecimal() and len(post_code_separated[1]) == 3 \
    #                                     else False

    def validate_address(self):
        # CITY
        while not (self.city.isalpha() and 2 < len(self.city) < 25):
            print('Wrong data format')
            self.city = input('Enter city name: ')

        # POSTAL CODE
        post_code_separated = self.post_code.split('-')
        while not (post_code_separated[0].isdecimal() and len(post_code_separated[0]) == 2 and
                   post_code_separated[1].isdecimal() and len(post_code_separated[1]) == 3):
            print('Wrong data format')
            self.post_code = input('Enter valid post code: ')
            post_code_separated = self.post_code.split('-')

        # STREET NAME
        while not (self.street.isalpha() and 2 < len(self.street) < 25):
            print('Wrong data format')
            self.street = input('Enter street name: ')

        # HOME NUMBER
        while not (self.home_number.isdecimal()):
            print('Wrong data format')
            self.home_number = input('Enter your home number: ')

        self.full_address()

    def validate_phone(self):
        self.phone = self.phone.replace(' ', '')
        while not (self.phone.isnumeric() and len(self.phone) == 9):
            print('Wrong data format')
            self.phone = input('Enter your phone: ')

    def validate_salary(self):
        while int(self.salary) < 5500:
            print('You know we can pay you more, right?')
            self.salary = input('Think about that one more time: ')
        while int(self.salary) > 6500:
            print('You know we can\'t pay you that much, right?')
            self.salary = input('Think about that one more time: ')

    def multi_validate(self):
        self.validate_name()
        self.validate_surname()
        self.validate_address()
        self.validate_phone()
        self.validate_salary()

    def change_data(self):
        change = 'y'
        while change not in ['n', 'no']:
            change = input('Do you want to change something? (y/n): ')
            if change in ['y', 'ye', 'yes']:
                choice = input('Which data you would like to change (name/surname/address/phone/salary): ').lower()
                # if choice == 'name':W
                if re.search('^n', choice):
                    self.name = input('Enter your name: ')
                if re.search('^su', choice):
                    self.surname = input('Enter your surname: ')
                if re.search('^a', choice):
                    self.city = input('Enter your address (city): ')
                    self.post_code = input('Enter your address (postal code): ')
                    self.street = input('Enter your address (street): ')
                    self.home_number = input('Enter your address (home number): ')
                    self.address = self.city + ' ' + self.post_code + ' ' + self.street + ' ' + self.home_number
                if re.search('^p', choice):
                    self.phone = input('Enter your phone: ')
                if re.search('^sa', choice):
                    self.salary = input('Enter what salary are you expecting: ')

                self.multi_validate()

    def print_data(self):
        print('Name: {}\nSurname: {}\nAddress: {}\nPhone Number: {}\nSalary: {}\n'
              .format(self.name.capitalize(), self.surname.capitalize(), self.address,
                      self.phone, self.salary))

    def organize_data(self):

        dict1 = {
            'Name': self.name.capitalize(),
            'Surname': self.surname.capitalize(),
            'Address': self.address.capitalize(),
            'Phone number': self.phone,
            'Salary': self.salary
        }

        return dict1


if __name__ == '__main__':
    add_user_param()
    # add_user()
    print_all()
    save_to_json()
    # save_to_excel()

# WALIDACJE OGARNĄĆ             ADRES   +
# ADRES PRZYJMOWAŁ RÓŻNE FORMATY ZAPISU, ALE ZAPIS PO SWOJEMU +
# PRZECHOWYWANIE DANYCH W PLIKU (MOŻE BYĆ JSON) +
# WYEKSPORTOWAĆ DO EXCELA


# inputy zamienić   +

# Sprawdź czu istnieją sys.argv     +
# argparse w main
# prostszy adres    +
# dekoratory na 2 / 3 validate
# generator danych zamiast inputów
