dct = {}

with open('en-ru.txt') as f:
    while True:
        ln = f.readline()

        if not ln:
            break

        fd = ln.split('-')
        fd[0] = fd[0].lstrip().rstrip()

        for i in fd[1].split(','):
            i = i.lstrip().rstrip()
            if i not in dct:
                dct[i] = [fd[0]]
            else:
                dct[i].append(fd[0])


with open('ru-en.txt', 'w') as f:
    for key, value in dct.items():
        f.write(key + ' - ' + ', '.join(value) + '\n')
