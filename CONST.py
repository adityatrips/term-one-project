import pickle
import os

db = 'db.dat'
bill = 'bills.dat'


def read_data(filename):
    if os.path.isfile(filename):
        data = None
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    else:
        data = []
        while True:
            try:
                with open(db, 'wb+') as file:
                    pickle.dump([], file)
                    break
            except EOFError as e:
                print(f'EOFError: {e}')
                break
        return data


def write_data(filename, data):
    while True:
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
                break
        except EOFError as e:
            print(f'EOFError: {e}')
            break


def gen_cst_bill(ident, name, phno, email, qty, total, sel_game):
    with open(f'{ident}.txt', 'w') as file:
        file.write('Games & Other Stuff\n')
        file.write(f'Bill issued to: {name}\n')
        file.write(f'Unique identification number: {ident}\n')
        file.write(f'Game\'s name: {sel_game["name"]}\n')
        file.write(f'Owner\'s phone number: {phno}\n')
        file.write(f'Owner\'s email address: {email}\n')
        file.write(f'Bought quantity: {qty}\n')
        file.write(f'Unit price: {sel_game["price"]}\n')
        file.write(f'Total: {sel_game["price"]} X {qty} = {total}\n')
        file.write("Thanks for shopping with us!\n")
