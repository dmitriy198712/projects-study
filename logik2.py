print("введите латинское слово")
word=input()
print(word)
a=word.count('a')
e=word.count('e')
i=word.count('i')
o=word.count('o')
u=word.count('u')
y=word.count('y')
if a==0:
    print("a=False")
elif e==0:
    print("e=false")
elif i==0:
    print("i=false")
elif o==0:
    print("o=false")
elif u==0:
    print("u=false")
elif y==0:
    print("y=false")
print(f"Гласных:{a+e+i+o+u+y}")
    