n=5
sph=[12, 55, 76, 33, 25]
hs=[6, 30, 34, 55, 32]
res=[]
for i in range(n):
    r=sph[i]*hs[i]
    res.append(r)

res.sort()
print(res)