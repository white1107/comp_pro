
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """20
SRSRSSRSSSRSRRRRRSRR




"""
input = get_input(INPUT)

###############################
n = int(input())
s = input()
ans = [0,0]
t= 0
ch = [[1,0],[0,-1],[-1,0],[0,1]]
tmp = ch[t]
for i in s:
    if i == "S":
        ans[0]+=tmp[0]
        ans[1]+=tmp[1]
    else:
        t +=1
        t%=4
        tmp =ch[t]
print(*ans) 