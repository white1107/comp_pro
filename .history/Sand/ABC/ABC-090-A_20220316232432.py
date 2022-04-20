
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """8 4
1 3 5 7 9 11 13 15


"""
input = get_input(INPUT)

###############################
from bisect import bisect_left

n,k = map(int,input().split())
a = list(map(int,input().split()))

print(bisect_left(a,k))
