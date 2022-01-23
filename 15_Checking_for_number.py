# 15. Дано число. Проверить кратно ли оно 7 и 23

import random


def divis(numb, div):
    if (numb % div == 0):
        return True

    return False


number = random.randint(-1000, 1000)
print('Дано число: ', number)
div1 = 7
div2 = 23
if (divis(number, div1) and divis(number, div2)):
    print('Данное число кратно 23 и 7')
else:
    print('Данное число не является кратным 23 и 7')



