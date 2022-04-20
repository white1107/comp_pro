
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
869120000 998244353 777777777 123456789 100100100 464646464 987654321 252525252 869120001 1000000000
10
4229
20210406
1
268435456
3582
536870912
1000000000
869120
99999999
869120001


"""
input = get_input(INPUT)

###############################
n = int(input())
M = []
for i in range(n):
    tmp = [0,0]
    c,p = map(int,input().split())
    c-=1
    tmp[c]=p
    M.append(tmp)

arr = []
M.insert([0,0],0)
for h,i,j,k in zip(M,M[1:]):
    print(h)


