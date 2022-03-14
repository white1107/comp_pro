
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """152


"""
input = get_input(INPUT)

###############################

X=int(input())

S=float("inf")

for a in range(1,10):
    for d in range(-9,10):
        b=a
        T=b
        while 0<=(b+d)<10 and T<X:
            T=10*T+(b+d)
            b+=d
        if T>=X:
            S=min(S,T)

print(S)
