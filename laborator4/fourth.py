def del3(a):
    if a % 3 == 0:
        return 0
    else:
        return a % 3


def del100b(b):
    try:
        print(100 / b)
    except ZeroDivisionError:
        print('cannot del by 0')


try:
    num = int(input())
except ValueError:
    print('cannot parse string')

del100b(num)


def is_magic(x):
    if x[0] * x[1] == (x[2] % 100):
        return True
    return False


x = int(input().split('.'))
print(is_magic(x))


def happy(x):
    a, b = 0, 0
    for i in range(0, len(x) // 2):
        a += int(x[i])
    for i in range(0, len(x) // 2):
        b += int(x[len(x) // 2 + i])
    return a == b


print(happy('2222'))
