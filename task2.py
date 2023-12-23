from random import randint


n = int(input('Введите кол-во чисел>'))

x = []
for _ in range(n):
    x.append(randint(0, 100))

print(f'{n} случайных чисел от 0 до 100')
print(x)
