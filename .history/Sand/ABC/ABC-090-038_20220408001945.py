
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """R G B
R G B



"""
input = get_input(INPUT)

###############################
import math 
x,y = map(int,input().split())

def lcm(x,y):
    return (x*y) //math.gcd(x,y)
ans = math.lcm(x,y)

if ans > 10**18:
    print("Large")
else:
    print(ans)