# 22. Найти расстояние между точками в пространстве 2D/3D

import math
import random

def dist_two_points(x1, x2, y1, y2):
    ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return ab

def dist_three_points(x1, x2, y1, y2, z1, z2):
    abc = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return abc

x1 = random.randint(-10,10)
x2 = random.randint(-10,10)
y1 = random.randint(-10,10)
y2 = random.randint(-10,10)
z1 = random.randint(-10,10)
z2 = random.randint(-10,10)

print('Расстояние между точками в 2D-пространстве: ', dist_two_points(x1, x2, y1, y2))
print('Расстояние между точками в 3D-пространстве: ', dist_three_points(x1, x2, y1, y2, z1, z2))



