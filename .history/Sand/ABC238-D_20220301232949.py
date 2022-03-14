
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
201408139683277485 381410962404666524
360288799186493714 788806911317182736
18999951915747344 451273909320288229
962424162689761932 1097438793187620758

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