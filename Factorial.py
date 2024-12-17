"""

Factorial of a number

"""

def factorial(n):
    #Base Case 
    if n == 0:
        return 1

    return n * factorial(n-1)

n = 5
answer = factorial(n)
print(answer)
