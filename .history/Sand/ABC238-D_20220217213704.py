
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
90 180 45 195



"""
input = get_input(INPUT)

###############################
n = int(input())
A = list(map(int,input().split()))

res = [0]

for I in A:
    for i in range(len(res)):
        res[i] += I
    res.append(0)

for i in range(len(res)):
    res[i]%=360


res.sort()

res.append(360)

m = 0

for i,j in zip(res,res[1:]):
    m = max(m,j-i)


print(m)
