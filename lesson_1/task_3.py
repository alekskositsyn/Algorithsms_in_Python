# 3.По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
#  https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing


print("Введите координаты точки А:")
x1 = int(input('x1: '))
y1 = int(input('y1:'))

print("Введите координаты точки B:")
x2 = int(input('x2: '))
y2 = int(input('y2:'))

if x1 == x2:
    print(f'x = {x1:.3f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k}x + {b}')
