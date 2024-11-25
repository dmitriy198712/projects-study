a=int(input("введите целое число"))
b=int(input())
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')