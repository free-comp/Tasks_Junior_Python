# 21. Программа проверяет пятизначное число на палиндромом.

def pldr(number):
    number = abs(number) # на случай ввода отрицательного числа
    first = number % 10
    second = (number % 100 - number % 10)//10
    fourth = (number % 10000 - number % 1000)//1000
    fifth = (number % 100000 - number % 10000)//10000

    if (first == fifth and second == fourth):
        return True
    
    return False

numb = int (input ('Введите пятизначное число: '))
if (pldr(numb)):
    print ('Введенное число является палиндромом.')
else:
    print ('Введенное число не является палиндромом.')