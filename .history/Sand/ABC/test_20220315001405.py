
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
2 3 2 3 3 3 2 3 3 2

"""
input = get_input(INPUT)

###############################

# a,b,c,x = map(int,input().split())

# if x<=a:print(1)
# elif a+1<= x <= b:
#   print(c/(b-a))
# else:
#   print(0)


# s = input()

# s = list(s)
# s.sort()
# # print(s)
# print("".join(s))

# a = list(map(int,input().split()))
# t = 0
# for i in range(3):
#   t = a[t]
# print(t)


# N = int(input())
# s = []
# ans = []
# tmpl = []
# for i in range(N):
#   a,b = map(int,input().split())
#   s.append([a,1])
#   s.append([a+b,-1])

# res = [0]*(N+1)
# p = 0
# d = 0
# t = i
# s.sort()
# for i,j in s:
#   res[d] += i - p
#   d += j
#   p = i
# print(*res[1:])


n = int(input())
l = list(map(int,input().split()))

dp = []
ans = 0
for i in l:
  if len(dp) >=1:q,p = dp.pop()
  else:q,p = 0,0
  # print(i,p,q)
  if q == 0: q=i;p=1;ans+=1;dp.append([i,1])
  elif q == i and p == i: ans -=i
  else:dp.append([q,p]);dp.append([i,1]);ans+=1
  print(ans)
