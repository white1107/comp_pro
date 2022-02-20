def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """6 1
350 350 70 2 3 4"""
input = get_input(INPUT)

###############################