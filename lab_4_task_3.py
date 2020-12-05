m = float(input("Масса тела: "))
h = float(input("Высота полёта: "))
v = float(input("Скорость: "))
g = 10
def energy(m, h, v, g):
  e1 = m * g * h
  e2 = (m * v ** 2) / 2
  x = e1 + e2
  return x
tmp = energy(m, h, v, g)
print(tmp)