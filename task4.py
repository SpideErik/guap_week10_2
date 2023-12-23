from random import randint


values = []
for _ in range(50):
    values.append(randint(1, 100))
print(f'Исходный список: {values}')

n = int(input('Введите n>'))
x = int(input('Введите число>'))

mult = []
for i in values:
    if i % x == 0:
        mult.append(i)
        if len(mult) >= n:
            break

a = n - len(mult)
if a > 0:
    print(f'Не хватило {a}')
if mult:
    print(f'Список кратных {x}: {mult}')
