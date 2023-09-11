import math
t = 1
xn = float(input('Введите переменную xn: '))
dx = float(input('Введите переменную dx: '))
x = xn

x1 = 'X'
y1 = 'Y'
symbol = '|'
print("{0:>10} {1:>13}".format(x1, y1))

for i in range(6):

    y = (math.log((x ** 3) + 3) + math.log(x, 10)) / (x * ((math.exp(x) - 1)))
    print('{0:>6} {1:.2f} | {2:>14.6f}'.format('|', x, y))
    x += dx
