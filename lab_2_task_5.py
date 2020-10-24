a = int(input('Введите a: '))
b = int(input('Введите b: '))

if b == 0:
    print('НЕЛЬЗЯ ДЕЛИТЬ НА НОЛЬ')
elif a % b == 0:
    print('Делится')
    print('Частное', a//b)
else:
    print('Не делится на целое')
    print('Остаток', a % b)