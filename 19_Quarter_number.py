# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, 
# причем X ≠ 0 и Y ≠ 0

def quart(x,y):
    if (x > 0 and y > 0):
        return 1
    elif (x > 0 and y < 0):
        return 2
    elif (x < 0 and y < 0):
        return 3
    else:
        return 4

import random

x = random.randint(-10,10)
y = random.randint(-10,10)

if (x == 0 or y == 0):
    print (f'Координаты точек x = {x}, y = {y}, номер четверти определить не получится. Попробуйте снова')
    exit()
print (f'Координаты точек x = {x}, y = {y}, что соответствует {(quart(x,y))} четверти системы координат')

