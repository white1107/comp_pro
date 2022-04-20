
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2 4


"""
input = get_input(INPUT)

###############################
l,r = map(int,input().split())
from collections import deque
def gcd(p,q):
    if p % q == 0:return q
    return gcd(q, p % q)


que = deque()
que.append([l,r])
while que:
    print(que)
    q,p = que.popleft()
    if gcd(p,q) == 1:
        print(p-q)
        exit()
    else:
        if q+1<= r:que.append([q-1,p])
        if p-1>= l:que.append([q,p-1])



