
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
1
2 6


"""
input = get_input(INPUT)

###############################
n = int(input())
M = []
for i in range(n):
    tmp = [0,0]
    c,p = map(int,input().split())
    c-=1
    tmp[c]=p
    M.append(tmp)

arr = []
M.insert(0,[0,0])
for h,i,j,k in zip(M,M[1:]):
    print(h)


