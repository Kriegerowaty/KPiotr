def change_data(n, s, a, p):
    change = ''
    while change != 'n' and change != 'no':
        change = input('Do you want to change something? (y/n): ')
        if change == 'y' or change == 'yes':
            choice = input('Which data you would like to change (name/surname/address/phone): ')
            if choice == 'name':
                n = input('Enter your name: ')
            if choice == 'surname':
                s = input('Enter your surname: ')
            if choice == 'address':
                a = input('Enter your address: ')
            if choice == 'phone':
                p = input('Enter your phone: ')

    print('\n', n, '\n', s, '\n', a, '\n', p)


def input_data():
    n = input("Enter your name: ")
    s = input("Enter your surname: ")
    a = input("Enter your address: ")
    p = input("Enter your phone: ")

    change_data(n, s, a, p)


if __name__ == '__main__':
    input_data()

