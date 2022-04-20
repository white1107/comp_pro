
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
a = list(map(str,input().split()))
b = list(map(str,input().split()))
t = 0
for i, j in zip(a,b):
    if i == j:t+=1

if t == 0:
    print('Yes')
elif t == 1:
    print('No')
elif t == 3:
    print('Yes')
