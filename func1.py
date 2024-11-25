

def factorial(n):

    if n == 0:

        return 1

    else:

        return n * factorial(n - 1)

 

def factorial_list(n):

    fact_n = factorial(n)

    factorials = []

    for i in range(fact_n, 0, -1):

        factorials.append(factorial(i))

    return factorials