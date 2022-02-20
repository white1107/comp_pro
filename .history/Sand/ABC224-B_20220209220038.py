def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3 3
2 1 4
3 1 3
6 4 1
"""
input = get_input(INPUT)

###############################

h,w = map(int,input().split())

l = []

for i in range(h):
    tmp = list(map(int,input().split()))
    l.append(tmp)
print(l)
for i in range(h-1):
    for j in range(w-1):
        print(l[i][j]+l[i+1][j+1]<=l[i+1][j]+l[i][j+1])