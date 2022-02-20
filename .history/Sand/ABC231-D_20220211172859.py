
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100

"""
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