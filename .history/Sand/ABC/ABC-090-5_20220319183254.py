
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10


"""
input = get_input(INPUT)

###############################
import bisect
n = int(input())
A = list(map(int,input().split()))
Q = int(input())
A.sort
for i in range(Q):
  b = int(input())
  t = bisect.bisect(A,b)
  if b ==0: print(abs(A[0]-b))
  elif b == len(A)-1:print(abs(A[-1]-b))
  else:min(abs(A[t]-b),abs(A[t+1]-b))
  