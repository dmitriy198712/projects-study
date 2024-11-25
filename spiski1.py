n=int(input())
sp=[]
for i in range(n):
    a=int(input())
    sp.append(a)
    sp.reverse()
print(*sp)