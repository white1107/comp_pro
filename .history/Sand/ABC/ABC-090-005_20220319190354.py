
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
ch ="atcoder"
dp = []
for i in range(n+10):
    dp.append([0,0,0,0,0,0,0,0])
for e,s in enumerate(S):
    if s == ch[0]: 
        print(e)
        dp[e][0] = 1
for i in range(0,8):
    for e,s in enumerate(S):
        if e==ch[i]:
            for ee,ss in enumerate(S[e+1:]):
                dp[ee+e][i+1]+=dp[e][i]

print(dp[-1])