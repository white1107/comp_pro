
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
from collections import defaultdict
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))


da = defaultdict(int)
db = defaultdict(int)
dc = defaultdict(int)


for i in range(n):
    A[i] = A[i]%46
    B[i] = B[i]%46
    C[i] = C[i]%46
    da[A[i]]+=1
    db[B[i]]+=1
    dc[C[i]]+=1


# print(da.keys())
# print(da.keys())
# print(da.keys())
ans = 0

for i in range(0,46):
    for j in range(0,46):
        ans += da[i]*db[j]*dc[(46-j-i)%46]
print(ans)
    
