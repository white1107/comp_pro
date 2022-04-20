
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5 1000000000
1 2 3 4 5


"""
input = get_input(INPUT)

###############################
from bisect import bisect_left

n,k = map(int,input().split())
a = list(map(int,input().split()))

ans = bisect_left(a,k)
if ans  == len(a):ans = -1
print(ans)
