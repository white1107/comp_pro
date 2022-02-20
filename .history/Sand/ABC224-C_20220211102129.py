def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
0 1
1 3
1 1
-1 -1

"""
input = get_input(INPUT)

###############################
from collections import Counter
n = int(input())

l = []

import numpy as np


def cal(e):
    if e>=3:res = e*(e-1)*(e-2)//6
    else: res = 0
    return res

for i in range(n):
    a,b = map(int,input().split())
    l.append(np.array([a,b]))

res = n*(n-1)*(n-1)
res //=6
for i in range(n):
    for j in range(i+1,n):
        for k  in range(j+1,n):
            a,b=l[j]-l[i],l[k]-l[i]
            print(np.outer(a,b))
            res -= np.outer(a,b)==0


print(res)