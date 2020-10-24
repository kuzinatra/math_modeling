a = int(input('Введите a: ')) #Первый член прогрессии
b = int(input('Введите b: ')) #Знаменатель
c = int(input('Введите c: ')) #Кол-во членов

print (a)
while c > 1:
    c = c - 1
    a = a * b
    print (a)