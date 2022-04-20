
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3


"""
input = get_input(INPUT)

###############################
h,w = map(int,input().split())
h = [0]*w
w = [0]*h
for i in range(h):
  a = list(map(int,input().split()))
  w[i] = sum(a)
  for e,i in enumerate(a):
    h[e]+=i


for e,i in enumerate(w):
  tmp = []
  for j in h:
    tmp.append(i+j)
  print(*tmp)