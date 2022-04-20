
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
dp = [0,0,0,0,0,0,0,0]*(10**5+10)
for e,s in enumerate(S):
    if s == ch[0]: dp[0][e] = 1
for i in range(8):
    for e,s in enumerate(S):
        if e==ch[i]: dp[i]