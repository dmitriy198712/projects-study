n=int(input("Введи число"))
a=0
for i in range (1, n+1):
    b=int(input("Введи целое число"))
    if b==0:
        a+=1
print(a)