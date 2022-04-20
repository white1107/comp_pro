
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """31
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
8 16
8 17
9 18
9 19
10 20
10 21
11 22
11 23
12 24
12 25
13 26
13 27
14 28
14 29
15 30
15 31


"""
input = get_input(INPUT)

###############################
n = int(input())

dic = []
for i in range(n):
  dic.append([])
for i in range(n-1):
  a,b = map(int,input().split())
  dic[a-1].append(b-1)
  dic[b-1].append(a-1)

que = [0]
ans = [0,0]
ch = [-1]*n
ch[0]=0
while que:
  q = que.pop()
  tar = dic[q]
  s = ch[q]
  for i in tar:
    if ch[i]==-1:
      ch[i]= s+1
      que.append(i)
      if ans[0] < ch[i]:
        ans = [ch[i],i]

print(ans)


que = [ans[1]]
ans = [0,0]
ch = [-1]*n
ch[que[0]]=0
while que:
  q = que.pop()
  tar = dic[q]
  s = ch[q]
  for i in tar:
    if ch[i]==-1:
      ch[i]= s+1
      que.append(i)
      if ans[0] < ch[i]:
        ans = [ch[i],i]

print(ans[0]+1)