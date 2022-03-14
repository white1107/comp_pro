
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """152


"""
input = get_input(INPUT)

###############################

import sys
sys.setrecursionlimit(10**6)

N,Q=map(int,input().split())
X=list(map(int,input().split()))
g=[[] for i in range(N)]
for i in range(N-1):
    A,B=map(int,input().split())
    A,B=A-1,B-1
    g[A].append(B)
    g[B].append(A)
d={}
def dfs(u,per=-1):
    l=[X[u]]
    for v in g[u]:
        if v==per:
            continue
        l+=dfs(v,u)
    l.sort(reverse=True)
    d[u]=l[:20]
    return l[:20]
dfs(0)
for i in range(Q):
    v,k=map(int,input().split())
    print(d[v-1][k-1])