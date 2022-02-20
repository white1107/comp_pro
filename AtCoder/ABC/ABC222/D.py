
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100


"""
input = get_input(INPUT)

###############################

mod = 998244353

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


dp = [1] + [0] * n
for i in range(3001):
    for j, (a, b) in enumerate(zip(A, B)):
        if a <= i <= b:
            dp[j + 1] += dp[j]
            dp[j + 1] %= mod

print(dp[n])
# print(ans[:10])