
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2
1 1
2 3


"""
input = get_input(INPUT)

###############################

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


mod = 998244353

ans = [1] + [0]*3000

for i in range(n-1):
  for j in range(a[i]-1,b[i]):
    for k in range(max(j,a[i+1]-1),b[i+1]):
      ans[k] += ans[j]
      print(ans[:10],i,j,k)


print(sum(ans[a[-1]-1:b[-1]]))

print(ans[:10])