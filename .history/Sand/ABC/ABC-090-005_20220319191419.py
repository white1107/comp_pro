
from sympy import Mod


def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr

"""
input = get_input(INPUT)

###############################
n = int(input())
S = input()
M = 10**9+7
ch ="atcoder0"
dp = []
for i in range(7):
    dp.append([0]*n)
for e,s in enumerate(S):
    if s == ch[0]: 
        dp[0][e] = 1
for i in range(0,7):
    for e,s in enumerate(S):
        if s==ch[i]:
            # print(i,e)
            for ee,ss in enumerate(S[e+1:]):
                # print(s,S[ee+e+1])
                if S[ee+e+1]==ch[i+1]:
                    # print(S[ee+e+1],dp[e][i])
                    dp[i+1][ee+e+1]+=dp[i][e]
                    dp[i+1][ee+e+1]%=M

print(sum(dp[-1]%M)