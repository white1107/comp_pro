
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """152


"""
input = get_input(INPUT)

###############################

from array import array
import bisect

Q = int(input())
query = []
X = set()

for i in range(Q):
    query.append(list(map(int, input().split())))
    X.add(query[i][1])

X = sorted(X)
idx = {x: i for i, x in enumerate(X)}

a = array('I', [])

for q in query:
    c = q[0]
    ix = idx[q[1]]

    if c == 1:
        bisect.insort(a, ix)
    
    elif c == 2:
        k = q[2]
        i = bisect.bisect(a, ix)
        print(X[a[i-k]] if 0 <= i-k else -1) 
    
    elif c == 3:
        k = q[2]
        i = bisect.bisect_left(a, ix)
        print(X[a[i+k-1]] if i+k-1 < len(a) else -1) 
