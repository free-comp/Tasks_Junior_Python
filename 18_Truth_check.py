# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def expres1(x, y):
    result = not (x or y)
    return result

def expres2(x, y):
    result = not x and not y
    return result

def print_result(x, y):
    print(f'При значении x = {x}, y = {y}')
    if (expres1(x, y) == expres2(x, y)):
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')

print_result(True, True)
print_result(True, False)
print_result(False, True)
print_result(False, False)

# через ввод:
# x = int (input('Для х введите 0 или 1: '))
# y = int (input('Для y введите 0 или 1: '))
# print (f'При значении x = {x}, y = {y}')

# if (expres1(x,y) == expres2(x,y)):
#     print ('Утверждение истинно')
# else:
#     print ('Утверждение ложно')
