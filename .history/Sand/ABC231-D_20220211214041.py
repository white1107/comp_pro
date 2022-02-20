
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4 3
1 4
2 4
3 4


"""
input = get_input(INPUT)

###############################

n,m = map(int,input().split())
s = []
res = [0]*(10**5+1)
f = 0
for i in range(m):
    a,b = map(int,input().split())
    res[a]+=1
    res[b]+=1
    if res[a]>3 or res[b]>3:f=1
    
if sum(res)>=2*n:f=1

if f:print("No")
else:print("Yes")