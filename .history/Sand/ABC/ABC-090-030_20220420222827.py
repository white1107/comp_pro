
from sympy import Mod


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """15 2

"""
input = get_input(INPUT)

###############################
n,k = map(int,input().split())

dp = [1]*(n+3)

for i in range(n+1):
    if i>=2:
        for j in range(j,n+1,j):
            dp[j] += 1
ans = 0    
for i in range(2,n+1):
    dp[i]>= k:ans+=1
print(ans) 