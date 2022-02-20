def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0


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
    l.append([a,b])

res = n*(n-1)*(n-2)
res //=6
# print(res)
for i in range(n):
    for j in range(i+1,n):
        for k  in range(j+1,n):
            a,b=l[j]-l[i],l[k]-l[i]
            # print(np.cross(a,b))
            res -= np.cross(a,b)==0


print(res)