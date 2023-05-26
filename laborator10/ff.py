import json

with open('products.json', 'r+') as fil:
    ljs = json.load(fil)

for t in ljs['products']:
    print('Название:', t['name'])
    print('Цена:', t['price'])
    print('Вес: ', t['weight'])
    if t['available']:
        print('В наличии')
    else:
        print('Нет в наличии')


nm = input()
pr = input()
wei = input()
avl = input()

ljs['products'].append(
    {'name': f'{nm}', 'price': f'{pr}', 'weight': f'{wei}', 'available': f'{avl}'}
)

print(ljs)