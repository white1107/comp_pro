
from this import d
from sympy import Mod


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3
10 13 93
5 27 35
55 28 52
"""
input = get_input(INPUT)

###############################
from collections import defaultdict
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))


da = defaultdict(int)
db = defaultdict(list)
dc = defaultdict(list)


for i in range(n):
    A[i] = A[i]%46
    B[i] = B[i]%46
    C[i] = C[i]%46
    da[A[i]]+=1
    db[B[i]]+=1
    dc[C[i]]+=1



ans = 0

for i in range(0,46):
    for j in range(0,46):
        ans += da[i]*db[j]*dc[(46-j)%46]
print(ans)
    
