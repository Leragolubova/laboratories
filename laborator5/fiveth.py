arr = [10, 20, 30, 30, 20]
ch = int(input())
if arr.count(ch):
    print(str(arr) + str(ch) + 'Поздравляю! Вы угадали число!')
else:
    print(str(arr) + str(ch) + 'Нет такого числа!')


chis = [1, 2, 1, 1, 3, 4, 5, 6, 7, 7]
for i in chis:
    if chis.count(i) > 1:
        print(i)


days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
n = int(input())
print('Ваши выходные дни: ')
for i in range(len(days) - 1, len(days) - n - 1, -1):
    print(days[i])
print('Ваши рабочие дни: ')
for i in range(0, len(days) - n):
    print(days[i])


f = ['Q', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
af = ['Ww', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj']
sf = (f[2], f[3], f[4], f[1], f[7], af[7], af[5], af[4], af[1], af[0])
print(str(f) + str(af) + str(sf))
print(len(sf))
sf = sorted(sf)
print(str(sf))
print(sf.count('Иванов'))
