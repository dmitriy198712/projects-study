print("введите число")
a=int(input())
if a%2==0 and a>0:
    print("Положительное четное число")
elif a==0:
    print("Нолевое значение")
elif a%2==0 and a<0:
    print("Отрицательное четное число")
else:
    print("число не является четным")


