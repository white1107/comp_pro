
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """314159265358979323846264338327950288419716939937510



"""
input = get_input(INPUT)

###############################

ans = 0

s = input()
n = len(s)
t = int(s)
s = s[::-1]

tmp = 0
for i in s:
  tmp += int(i)
ans += tmp
for i in range(n-1):
  tmp -= int(s[i]) 
  ans += tmp*(10**(i+1))
  # print(ans)

print(ans)

