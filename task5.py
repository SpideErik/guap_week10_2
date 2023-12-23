from random import choice

names = ['камень', 'ножницы', 'бумага']
pc = choice(names)

user = input('Ваш ход>').lower()
if user in "123":
    user = names[int(user) - 1]
elif user not in names:
    print('Ошибка')
    exit()

win = 'Вы выиграли'
if ((pc == 'камень' and user == 'ножницы') or
        (pc == 'ножницы' and user == 'бумага') or
        (pc == 'бумага' and user == 'камень')):
    win = 'Компьютер выйграл'
elif pc == user:
    win = 'Ничья'

print(f'Ход компьютера: {pc.title()}')
print(f'Ваш ход: {user.title()}')
print(win)
