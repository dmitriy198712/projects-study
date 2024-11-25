x=int(input("введите число"))
s=0
for b in range(1, x+1):
    if x%b==0:
        s=s+1
    print(s)