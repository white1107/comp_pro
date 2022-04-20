
from sympy import Mod


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """869120 1



"""
input = get_input(INPUT)

###############################
n,k = map(int,input().split())

dp = [0]*(n+3)

for i in range(2,n+1):
    if dp[i]==0:
        for j in range(i,n+1,i):
            dp[j] += 1
ans = 0    
for i in range(2,n+1):
    if dp[i]>=k:ans+=1
print(ans) 
# print(dp)