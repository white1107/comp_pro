def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """atcoder"""
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
        print(l[i][j])