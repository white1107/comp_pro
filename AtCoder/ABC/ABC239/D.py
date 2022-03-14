
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3 14 1 5



"""
input = get_input(INPUT)

###############################

def list_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            elif i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes

n = 1000
list_p = list_primes(n)

a,b,c,d = map(int,input().split())

flag = 1
for i in range(a,b+1):
    t_flag = 0
    for j in range(c,d+1):
        if i+j not in list_p :t_flag += 1
    if t_flag == d-c+1:flag= 0

if flag:print("Aoki")
else:print("Takahashi")