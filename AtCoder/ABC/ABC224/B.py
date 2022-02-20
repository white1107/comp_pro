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

h,w = map(int,input().split())

l = []
flag = True
for i in range(h):
    tmp = list(map(int,input().split()))
    l.append(tmp)
# print(l)
for i in range(h-1):
    for j in range(w-1):
        if not l[i][j]+l[i+1][j+1]<=l[i+1][j]+l[i][j+1]:flag = False

if flag:print("Yes")
else:print("No")