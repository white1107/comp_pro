
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
1 2
1 3
2 4
4 5
4 6
3 7
7 8
8 9
8 10


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