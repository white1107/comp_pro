def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """atcoder"""
input = get_input(INPUT)

###############################


s =  input()

if s[-2:] == 'er':print('er')
else:print("ist")