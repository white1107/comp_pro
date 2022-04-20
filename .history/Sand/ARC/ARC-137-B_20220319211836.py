
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954


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
    if zc ==0 and i == 0: zc = 1
    elif oc == 0 and i == 0:oc = 1
    
    if i == j and i == 0:zc+=1
    elif i == j and i == 1:oc+=1
    elif i != j and i == 0:zc = 0
    elif i != j and i == 1:oc = 0

    z = max(z,zc)
    o = max(o,oc)


print(z,c)