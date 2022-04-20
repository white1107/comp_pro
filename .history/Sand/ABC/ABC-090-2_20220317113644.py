
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954


"""
input = get_input(INPUT)

###############################
n = int(input())

if n%2==0:
  for i in range(2**n):
    print(str(bin(i)))