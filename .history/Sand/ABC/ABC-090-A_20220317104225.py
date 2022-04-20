
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3 34
1
8 13 26

"""
input = get_input(INPUT)

###############################
n,L = map(int,input().split())
K = int(input())
a= list(map(int,input().split()))
ans = float('INF')
def is_ok(k):
    a = [0] + a+[L]
    t = 0
    count = 0
    for e,i in enumerate(a[1:-1]):
        t += i-a[e]
        if t>k:count+=1;ans=min(ans,t);t=0
    if count >= K+1:return ans
    else:return 0

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(1,10**9))