
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """1
0 0 0 0 0 0 0 



"""
input = get_input(INPUT)

###############################
n = int(input())
A = list(map(int,input().split()))
A.append(2)
z = 0
o = 0
zc = 0
oc = 0
for i,j in zip(A,A[1:]):
    # print('ind',i,j)
    if i == 1:oc =max(1,oc)
    if j == 0:zc = max(1,zc)
    z = max(z,zc)
    o = max(o,oc)
    if i == j and i == 0:zc+=1
    elif i == j and i == 1:oc+=1
    elif i != j and i == 0:zc = 0
    elif i != j and i == 1:oc = 0

    z = max(z,zc)
    o = max(o,oc)
    # print(z,o)

print(z+o+1)