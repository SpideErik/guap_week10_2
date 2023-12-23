from random import choice


words = input('Введите размер A B>').split()
a = int(words[0])
b = int(words[1])

words = input('Введите позицию робота X Y>').split()
x = int(words[0])
y = int(words[1])
if x < 0 or x >= a or y < 0 or y >= a:
    print('Робот за пределами поля')
    exit()

n = int(input('Введите кол-во ходов n>'))

moves = [(0, 1, 'вверх'), (0, -1, 'вниз'), (-1, 0, 'влево'), (1, 0, 'вправо')]

zone = []
for _ in range(b):
    zone.append(['o']*a)
fill = 1
zone[y][x] = 'x'
print('Карта в момент высадки')
for i in range(b):
    for j in range(a):
        print(zone[i][j], end='')
    print()


for i in range(1, n+1):
    dx, dy, name = choice(moves)
    x += dx
    y += dy
    print(f'Ход {i}: {name}, новые координаты {x},{y}')
    if x < 0 or x >= a or y < 0 or y >= a:
        print(f'Робот вышел за пределы за {i} ходов')
        break
    if x == 0 or y == 0 or x == a-1 or y == b-1:
        print('Робот на границе')
    if zone[y][x] == 'o':
        zone[y][x] = 'x'
        fill += 1
    else:
        print('Здесь уже были')
else:
    print('Миссия завершена успешно')

print(f'Исследовано {100 * fill / (a*b)}%')
print('Исследованная Карта')
for i in range(b):
    for j in range(a):
        print(zone[i][j], end='')
    print()
