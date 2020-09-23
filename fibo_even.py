# Написать функцию, которая бы выводила только четные числа в методе Фибоначи
# пример :f(4) = 0,2,8,32

def fib(n):
    if n < 2:
        quit()
    
    f1 = f2 = 1
    farr = [0]
    i = len(farr)

    while i < n:
        f1, f2 = f2, f1 + f2
        if f2 % 2 == 0:
            farr.append(f2)
            i = i + 1
    
    print(farr)

n = int(input('Введите число: '))
fib(n)

