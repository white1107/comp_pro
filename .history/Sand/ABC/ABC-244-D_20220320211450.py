
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7



"""
input = get_input(INPUT)

###############################
a = list(map(int,input().split()))
b = list(map(int,input().split()))
t = 0
for i, j in zip(a,b):
    if i == j:t+=1

if t == 0:
    print('Yes')
elif t == 1:
    print('No')
elif t == 3:
    print('Yes')
