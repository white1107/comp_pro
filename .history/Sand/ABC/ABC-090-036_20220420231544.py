
from this import d
from sympy import Mod


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """20
238 395 46 238 264 114 354 52 324 14 472 64 307 280 209 24 165 194 179 248
270 83 377 332 173 21 362 75 66 342 229 117 124 481 48 235 376 13 420 74
175 427 76 278 486 169 311 47 348 225 41 482 355 356 263 95 170 156 340 289


"""
input = get_input(INPUT)

###############################
n,q=map(int,input().split())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a-b)
    y.append(a+b)
x_max=max(x)
x_min=min(x)
y_max=max(y)
y_min=min(y)
for i in range(q):
    j=int(input())-1

    ans = max(abs(x[j]-x_max),abs(x[j]-x_min),abs(y[j]-y_max),abs(y[j]-y_min))
    print(ans)