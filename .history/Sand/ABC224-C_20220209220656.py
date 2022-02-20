def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2 4
4 3 2 1
5 6 7 8

"""
input = get_input(INPUT)

###############################
from collections import Counter
n = int(input())

x = []
y = []

for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)


cx = Counter(x)
cy = Counter(y)

print(cx,cy)