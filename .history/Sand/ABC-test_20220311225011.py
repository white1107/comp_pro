
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """aba







"""
input = get_input(INPUT)

###############################

# a,b,c,x = map(int,input().split())

# if x<=a:print(1)
# elif a+1<= x <= b:
#   print(c/(b-a))
# else:
#   print(0)


s = input()

s = list(s)
s.sort()
# print(s)
print("".join(s))

