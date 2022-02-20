def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """atcoder"""
input = get_input(INPUT)

###############################


n = int(input())
s = []
for i in range(n):
    a,b = map(int,input().split())
    s.append([a,1])
    s.append([a+b,-1])
    
res = [0]*(n+1)
p=0
d=0
s.sort()

for i,j in s:
    res[p]+=i-d
    p+=j
    d=i

print(*res[1:])