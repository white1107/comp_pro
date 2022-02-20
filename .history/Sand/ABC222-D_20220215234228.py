
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

ans = [0]*3001
for j in range(a[0],b[0]+1): 
  ans[j] += 1
print(ans[:10])
for i in range(1,n-1):
  for j in range(a[i],b[i]+1):
    for k in range(max(j,a[i+1]),b[i+1]+1):
      if k==j:ans[k] = ans[j]
      else:ans[k]+= ans[j]
      print(ans[:10],i,j,k)

print(ans[:10])
print(sum(ans[a[-1]:b[-1]+1]))
print(a[-1],b[-1])

# print(ans[:10])