
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """1225

"""
input = get_input(INPUT)

###############################

ans = 0

s = input()
n = len(input())
t = int(s)
s = s[::-1]

tmp = 0
for i in s:
  tmp += int(i)
ans += tmp
for i in range(1,n):
  tmp -= int(s[i]) 
  ans += tmp*10

print(ans)

