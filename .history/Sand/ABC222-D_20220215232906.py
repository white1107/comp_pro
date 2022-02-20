
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

for i in range(n-1):
  for j in range(a[i]-1,b[i]):
    for k in range(a[i+1]-1,b[i+1]):
      ans[k] += ans[j]


print(sum(ans[a[-1]-1:b[-1]]))