
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4

"""
input = get_input(INPUT)

###############################
n = int(input())

if n%2==0:
  for i in range(2**(n-1),2**n):
    print(str(bin(i))[2:])