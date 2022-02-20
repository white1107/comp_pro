
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

a,N = map(int,input().split())

que = [N,0]
while que:
    q,s = que.pop()
    if q == N:
        print(s)
        exit()
    if not q%10== 0 and not len(str(q))==1:
        for i in len(str(q)):



print(-1)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mod = 998244353

ans = [1] + [0]*n

for i in range(3001):
  for j in range(1,n+1):
    if a[j-1] <= i <= b[j-1]:
      ans[j] += ans[j-1]
      ans[j] %= mod

print(ans[n])