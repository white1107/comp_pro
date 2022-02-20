
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """16



"""
input = get_input(INPUT)

###############################
n = input()

s = len(n)


res =0

def cal(d):
    S = len(str(d))
    tmp = 10**(S-1)
    mp = d-tmp+1
    return mp*(1+mp)//2

print(cal(9)+cal(16))

# for i in range(1,s):
#     res += 