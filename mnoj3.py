print("введите в строку последовательность чисел")
sp1=list(map(int,input().split()))
x=set(sp1)
a=set()
for i in x:
    if i not in x:
        a.add(i)
        print("NO")
    else:
        print("YES")

