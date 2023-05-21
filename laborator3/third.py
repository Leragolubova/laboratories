n = int(input())
b = ""
for i in range(n):
    x = input()
    b = b + " " + x
print(b)
b = ""
while True:
    a = input()
    if a != "stop":
        b = b + " " + a
    else:
        break
print(b)
while True:
    a = input()
    if a.count('ф'):
        print("Ого, это редкое слово")
    else:
        print("Эх, это не очень редкое слово...")
        
        
from random import randint

print('Давайте поиграем')
rez = 0
prav_otv = 0
while True:
    x = randint(1, 123)
    y = randint(1, 123)
    print(x + "+" + y + "=", end="")
    rez =  int(input())

    if x + y == rez:
        prav_otv += 1
        print("Правильно!")
    else:
        rez += 1
        print("Ответ неправильный!")

    if rez == 3:
        print('Игра окончена. Правильных ответов:' + prav_otv)
