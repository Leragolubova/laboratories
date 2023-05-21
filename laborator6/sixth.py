c = {}
c['Россия'] = 'Москва'
c['Франция'] = 'Париж'

for key, value in c.items():
    print(key, value)
print(c['Франция'])

sd = sorted(c, key=c.get)
print(*sd)


cst = {}
cst['Ф'] = cst['Щ'] = cst['Ъ'] = 10
cst['Ш'] = cst['Э'] = cst['Ю'] = 8
cst['Ж'] = cst['З'] = cst['Ч'] = cst['Ц'] = cst['Х'] = 5
cst['Й'] = cst['Ы'] = 4
cst['Б'] = cst['Г'] = cst['Ё'] = cst['Ь'] = cst['Я'] = 3
cst['Д'] = cst['К'] = cst['Л'] = cst['М'] = cst['П'] = cst['У'] = 2
cst['А'] = cst['В'] = cst['Е'] = cst['И'] = cst['Н'] = cst['О'] = cst['Р'] = cst['С'] = cst['Т'] = 1

an = input()
ans = 0
for i in an:
    i = i.upper()
    ans += cst[i]
print(ans)


stud = {}
stud['Артём'] = ['Китайский', 'Русский']
stud['Андрей'] = ['Английский']

ln = set()
jp = set()
for key, value in stud.items():
    for j in value:
        ln.add(j)
        if j == 'Китайский':
            jp.add(key)

print(*ln)
print(*jp)
