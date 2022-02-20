def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
0 1
1 3
1 1
-1 -1

"""
input = get_input(INPUT)

###############################
from collections import Counter
n = int(input())

x = []
y = []


def cal(e):
    if e>=3:res = e*(e-1)*(e-2)//6
    else: res = 0
    return res

for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)


cx = Counter(x)
cy = Counter(y)

result = cal(n)
for i in cx:
    result -= cal(cx[i])

for i in cy:
    result -= cal(cy[i])

print(result)



