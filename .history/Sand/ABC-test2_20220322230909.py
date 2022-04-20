
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2
1000000000 1000000000
1000000000 1000000000



"""
input = get_input(INPUT)

###############################
