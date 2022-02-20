
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

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


mod = 998244353

ans = [1] + [0]*n

for i in range(3001):
  for j in range(0,n):
    if a[j] <= i <= b[j]:
      ans[j+1] += ans[j]
      ans[j+1] %= mod

print(ans[n])
