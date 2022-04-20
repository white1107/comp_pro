
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """1
0 1



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
if A[0] == 1:oc=1
else: zc=1

for i,j in zip(A,A[1:]):


   
    if i == j and j == 0:zc+=1
    elif i == j and j == 1:oc+=1
    elif i != j and j == 0:zc = 0
    elif i != j and j == 1:oc = 0

    z = max(z,zc)
    o = max(o,oc)
    # print(z,o)

print(z+o+1)