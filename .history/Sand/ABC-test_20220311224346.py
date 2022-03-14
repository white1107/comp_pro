
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """30 500 20 103




"""
input = get_input(INPUT)

###############################

a,b,c,x = map(int,input().split())

if a+1<= x <= b:
  print(c/(b-a))
else:
  print(x)
