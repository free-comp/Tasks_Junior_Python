# 17. По двум заданным числам проверять является ли одно квадратом другого.

def square(n1, n2):
    if (n1 == n2 ** 2):
        return True
    
    return False
    
        
numb1 = int(input ('Введите первое число: '))
numb2 = int(input ('Введите второе число: '))

if (square(numb1, numb2)):
    print ('Первое число является квадратом другого')
elif (square(numb2, numb1)):
    print ('Второе число является квадратом другого')
else:
    print ('Ни одно из чисел не является квадратом другого')
