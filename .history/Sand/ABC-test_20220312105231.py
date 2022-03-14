
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3
1 2
2 3
3 1


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


N = int(input())
s = []
ans = []
tmpl = []
for i in range(N):
  a,b = map(int,input().split())
  s.append([a,1])
  s.append([a+b,-1])

res = [0]*(N+1)
p = 0
d = 0
t = i
s.sort()
for i,j in s:
  res[d] += i - p
  d += j
  p = i
print(*res[1:])