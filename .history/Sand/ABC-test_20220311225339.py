
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """9 0 1 2 3 4 5 6 7 8








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

a = list(map(int,input().split()))
t = 0
for i in range(3):
  t = a[t]
print(t)
