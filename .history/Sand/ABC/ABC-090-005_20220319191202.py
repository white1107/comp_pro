
from sympy import Mod


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
attcordeer

"""
input = get_input(INPUT)

###############################
n = int(input())
S = input()
M = 10**9+7
ch ="atcoder0"
dp = []
for i in range(n):
    dp.append([0,0,0,0,0,0,0,0])
for e,s in enumerate(S):
    if s == ch[0]: 
        print(e)
        dp[e][0] = 1
for i in range(0,7):
    for e,s in enumerate(S):
        if s==ch[i]:
            # print(i,e)
            for ee,ss in enumerate(S[e+1:]):
                # print(s,S[ee+e+1])
                if S[ee+e+1]==ch[i+1]:
                    print(S[ee+e+1],dp[e][i])
                    dp[ee+e+1][i+1]+=dp[e][i]
                    dp[ee+e+1][i+1]%=M

print(dp)