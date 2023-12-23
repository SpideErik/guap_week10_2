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
else:
    print('Миссия завершена успешно')
