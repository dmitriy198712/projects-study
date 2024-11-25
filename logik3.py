print("Марина введи число")
invest=int(input())
Mike=int(input())
Ivan=int(input())
if (Mike>=invest) and (Ivan>invest):
    print(2)
elif (Mike>=invest):
    print("Mike")
elif (Ivan>=invest):
    print("Ivan")
elif Mike+Ivan>=invest:
    print("-1")
else:
    print(0)