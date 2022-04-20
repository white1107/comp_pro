
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
for i in itertools.zip_longest('12345','789'):
    print(i)