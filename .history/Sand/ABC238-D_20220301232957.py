
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2
1 8
4 2


"""
input = get_input(INPUT)

###############################

n = int(input())
for i in range(n):
  a,b = map(int,input().split())
  if a*2 <= b and (b-a*2)&a ==0:
    print("Yes")
  else:
    print("No")