
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """314159265358979323846264338327950288419716939937510



"""
input = get_input(INPUT)

###############################

a,b,c,x = map(int,input().split())

if a+1<= x <= b:
  print((b-a+1)/c)
else:
  print(x)
