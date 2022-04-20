
from sympy import prime


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """234





"""
input = get_input(INPUT)

###############################
k = int(input())
dp = [0]*(k+1)
M = 10**9+7
dp[0] = 1
for i in range(1,k+1):
    B = min(i,9)
    for j in range(1,B+1):
        dp[i] +=dp[i-j]
        dp[i]%=M
print(dp[k])