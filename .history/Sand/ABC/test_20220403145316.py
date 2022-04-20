
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
4
6 10 12 8
6
5 4 5 4 4 4
10
10 10 7 6 7 4 4 5 7 4
1
10




"""
input = get_input(INPUT)

###############################
import itertools



def backspaceCompare(S, T):
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

        for x, y in itertools.zip_longest(F(S), F(T)):
            print(x,y)

backspaceCompare("take","fine")