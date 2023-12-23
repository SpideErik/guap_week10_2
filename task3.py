from random import uniform

n = int(input('Введите кол-во чисел>'))

x = []
y = []
for _ in range(n):
    v = uniform(-100.0, 100.0)
    x.append(v)
    y.append(round(v))

print(f'Список случайных чисел {x}')
print(f'Список округленных чисел {y}')
