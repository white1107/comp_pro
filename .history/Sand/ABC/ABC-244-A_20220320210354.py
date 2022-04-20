
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