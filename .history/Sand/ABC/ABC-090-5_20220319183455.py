
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
869120000 998244353 777777777 123456789 100100100 464646464 987654321 252525252 869120001 1000000000
10
4229
20210406
1
268435456
3582
536870912
1000000000
869120
99999999
869120001


"""
input = get_input(INPUT)

###############################
import bisect
n = int(input())
A = list(map(int,input().split()))
Q = int(input())
A.sort()
for i in range(Q):
  b = int(input())
  t = bisect.bisect(A,b)
  # print(b,t)
  if t ==0: print(abs(A[0]-b))
  elif t == len(A)-1:print(abs(A[-1]-b))
  else:print(min(abs(A[t]-b),abs(A[t-1]-b)))
