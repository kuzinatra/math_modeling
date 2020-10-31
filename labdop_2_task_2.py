a = int(float(input('Введите a: ')))
b = int(float(input('Введите b: ')))
c = int(float(input('Введите c: ')))

if a+b<c or b+c<a or c+a<b or a+b==c or b+c==a or c+a==b:
    print ('Такого треугольника не существует')
else:
    if a==b==c:
        print('Равносторонний')
    elif a==b or b==c or c==a:
        print('Равнобедренный')
    else:
        print('Разносторонний')