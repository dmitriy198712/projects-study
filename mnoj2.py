print("введите список чисел")
sp1=list(map(int,input().split()))
print("введите второй список")
sp2=list(map(int,input().split()))
a=set(sp1)
b=set(sp2)
print(a.union(sp2))