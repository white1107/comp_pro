
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4

"""
input = get_input(INPUT)

###############################
n = int(input())

res = []
if n%2==0:
  for i in range(2**(n-1),2**n):
    t = str(bin(i))[2:]
    tmp = 0
    for j in t:
      if j =="1": tmp = tmp+1 
      else: tmp-=1
      if tmp <0:break
    if tmp==0:t=t.replace('1','(');t=t.replace('0',')');res.append(t)
res.sort()
print(res)
