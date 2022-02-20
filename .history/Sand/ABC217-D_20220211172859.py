
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2 4
4 3 2 1
5 6 7 8

"""
input = get_input(INPUT)

###############################

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [0]*3000

for i in range(n-1):
    a = A[i]
    c = A[i+1]
    b = B[i]
    d = B[i+1]
    f = d - c+1
    for j in range(a,c+1):
        dp[j] = 

