
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
m = [1]
print(1)
for i in range(n):
    t = int(input())
    m.append(t)
    if t== 0:exit()
    for j in range(2,1001):
        if j not in m:
            print(j)
            m.append(j) 