def cmp(x):
    return(x//10)* (x%10)

tmp=[11, 45, 66, 12, 87]
tmp.sort(key=cmp)

print(tmp)
