
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
4
6 10 12 8
6
5 4 5 4 4 4
10
10 10 7 6 7 4 4 5 7 4
1
10




"""
input = get_input(INPUT)

###############################



a = int(input())
for t in range(a):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        if ans<=l[i]:
            ans +=1
    print("Case #"+str(t)+": "+str(ans))
