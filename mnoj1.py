print("Введите количество чисел N")
n=int(input())
print("Введите в строку через пробел числа N < 2*10e9")
n1=list(map(int,input().split()))
spisok=set(n1)
print(len(spisok))

