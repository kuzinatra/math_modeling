from math import sqrt, pi
 
Фигура = (input("Фигура: "))

if Фигура == 'Круг':
  r = float(input("Радиус: "))
  def Круг(r):
    x = pi * r **2
    return x
  tmp = Круг(r)
  print(tmp)
elif Фигура == 'Прямоугольник':
    a = float(input("Длина: "))
    b = float(input("Ширина: "))
    def Прямоугольник(a,b):
      S = a * b
      return S
    tmp = Прямоугольник(a, b)
    print((tmp))
elif Фигура == 'Треугольник':
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    c = float(input("Третья сторона: "))
    def Треугольник(a, b, c):
      p = (a+b+c)/2
      S = sqrt(p*(p-a)*(p-b)*(p-c))
      return S
    tmp = Треугольник(a, b, c)
    print(tmp)