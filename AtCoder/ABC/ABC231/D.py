
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4 3
1 4
2 4
3 4


"""
input = get_input(INPUT)

###############################

belong=[]
group=[]

def init(X):
  global belong
  global group
  belong=list(range(X))
  group=[[i] for i in range(X)]

def unite(x,y):
  if len(group[belong[x]])<len(group[belong[y]]):
    x,y=y,x
  if belong[x]==belong[y]:
    return True
  z=belong[y]
  for i in range(len(group[z])):
    belong[group[z][-1]]=belong[x]
    group[belong[x]].append(group[z][-1])
    del group[z][-1]
  return False

N,M=map(int,input().split())
C=[0]*(N+1)
init(N+1)
for i in range(M):
  a,b=map(int,input().split())
  if unite(a,b):
    print('No')
    exit()
  C[a]+=1
  C[b]+=1
if max(C)<=2:
  print('Yes')
else:
  print('No')
