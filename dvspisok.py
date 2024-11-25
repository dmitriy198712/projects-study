import random

def pl(x):
    for i in x:
        print(*i)
h = int(input('h = '))

w = int(input('w = '))
matrix_1=[[random.randint(1, 11) for j in range(h)] for i in range(w)]
matrix_2=[[random.randint(1, 11) for j in range(h)] for i in range(w)]

res = [[matrix_1[i][j] + matrix_2[i][j]  for j in range

(len(matrix_1[0]))] for i in range(len(matrix_1))]

print("Результат сложения двух матриц: ")

for r in res:
  pl(res)