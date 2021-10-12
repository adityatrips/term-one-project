import time
import CONST
for i in '* Manav Rachna International School, Charmwood\n* Class XII Fleming\n* Aditya Tripathi & Prayag Jain\n* Ms. Preeti Tanjea':
    print(i, flush=True, end='')
    time.sleep(0.01)
print('\n')
print('1. Browse games')
print('2. Buy games')
print()
dec = int(input("Enter your decision\n\t=> "))
if dec == 1:
    data = CONST.read_data(CONST.db)
    print('*'*50)
    for d in data:
        print('*', 'Serial Number  :', d['sno'])
        print('*', 'Name           :', d['name'])
        print('*', 'Developer      :', d['dev'])
        print('*', 'Edition        :', d['edition'])
        print('*', 'Year of release:', d['year'])
        print('*', 'Price          :', d['price'])
        print('*', 'Stocks left    :', d['stock'])
        print('*'*50)
elif dec == 2:
    data = CONST.read_data(CONST.db)
    sno = input('Enter the serial number of the title you\'d like to buy\n\t=> ')
    av_sno = [d['sno'] for d in data]
    if sno not in av_sno:
        print('The title number you entered doesn\'t match any numbers in our database!')
    else:
        sel_game = None
        for d in data:
            if d['sno'] == sno:
                sel_game = d
        name = input('Enter your name\n\t=> ')
        ident = f'{"_".join(name.split())}_{"_".join(sel_game["name"].split())}_{round(time.time(), 2)}'
        phno = input('Enter your phone number\n\t=> ')
        email = input('Enter your email\n\t=> ')
        qty = input('Enter the quantity you\' like to buy\n\t=> ')
        if int(sel_game['stock']) < int(qty):
            print(f'Out of stock! Only {sel_game["stock"]} left')
        else:
            total = int(qty) * int(sel_game['price'])
            upd_qty = str(int(sel_game['stock']) - int(qty))
            for d in data:
                if d['sno'] == sno:
                    d['stock'] = upd_qty
            CONST.write_data(CONST.db, data)
            want_bill = input('Do you want a bill copy (y/n)\n\t=> ').lower()
            bills = CONST.read_data(CONST.bill)
            bills.append({
                'ident': ident,
                'owners_name': name,
                'sel_game_name': sel_game["name"],
                'owners_phno': phno,
                'owners_email': email,
                'bought_qty': qty,
                'unit_price': sel_game['price'],
                'total': total,
            })
            CONST.write_data(CONST.bill, bills)
            if want_bill == 'y':
                CONST.gen_cst_bill(ident, name, phno, email,
                                   qty, total, sel_game)
            else:
                print('Thanks for shopping with us!')
