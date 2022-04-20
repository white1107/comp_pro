
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5


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