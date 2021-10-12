from os import read
import time
import pickle
import CONST
for i in '* Manav Rachna International School, Charmwood\n* Class XII Fleming\n* Aditya Tripathi & Prayag Jain\n* Ms. Preeti Tanjea':
    print(i, flush=True, end='')
    time.sleep(0.01)
print('\n')
print('1. Add stock')
print('2. Update stock')
print('3. Browse bills')
print()
dec = int(input('Enter your decision\n\t=> '))
if dec == 1:
    sno = input('Enter the serial number\n\t=> ')
    name = input('Enter the name of the title\n\t=> ')
    dev = input('Enter the developer of the title\n\t=> ')
    edition = input('Enter the edition of release\n\t=> ')
    year = input('Enter the year of release\n\t=> ')
    price = input('Enter the price of one unit\n\t=> ')
    stock = input('Enter the available amount\n\t=> ')
    data = CONST.read_data(CONST.db)
    data.append({
        'sno': sno,
        'name': name,
        'dev': dev,
        'edition': edition,
        'year': year,
        'price': price,
        'stock': stock,
    })
    CONST.write_data(CONST.db, data)
elif dec == 2:
    sno = input('Enter the serial number of the title\n\t=> ')
    upd_stock = input('Enter the updated stock number\n\t=> ')
    data = CONST.read_data(CONST.db)
    for d in data:
        if d['sno'] == sno:
            d['stock'] = upd_stock
    CONST.write_data(CONST.db, data)
elif dec == 3:
    bills = CONST.read_data(CONST.bill)
    print('1. All bills')
    print('2. Search')
    b_dec = int(input('Enter your decision\n\t=> '))
    if b_dec == 1:
        print('*'*50)
        for d in bills:
            print('Identification number:', d['ident'])
            print('Owner\'s Name         :', d['owners_name'])
            print('Game\'s Name          :', d['sel_game_name'])
            print('Owner\'s Phone        :', d['owners_phno'])
            print('Owner\'s Email        :', d['owners_email'])
            print('Quantity Bought      :', d['bought_qty'])
            print('Total                :', d['total'])
            print('*'*50)
    elif b_dec == 2:
        ident = input('Enter the identification number\n\t=> ')
        for d in bills:
            if d['ident'] == ident:
                print('Owner\'s Name         :', d['owners_name'])
                print('Game\'s Name          :', d['sel_game_name'])
                print('Owner\'s Phone        :', d['owners_phno'])
                print('Owner\'s Email        :', d['owners_email'])
                print('Quantity Bought      :', d['bought_qty'])
                print('Total                :', d['total'])
                print('*'*50)
        else:
            print('No record found!')
