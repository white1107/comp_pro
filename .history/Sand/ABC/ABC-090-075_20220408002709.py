
from sympy import prime


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """100




"""
input = get_input(INPUT)

###############################
n = int(input())
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

ans = len(prime_factorize(n))

a = 0
t = 1
while t<ans:
    t *=2
    a +=1
print(a) 