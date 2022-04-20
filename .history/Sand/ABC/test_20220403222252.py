
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
# import itertools



# def backspaceCompare(S, T):
#     def F(S):
#         skip = 0
#         for x in reversed(S):
#             if x == '#':
#                 skip += 1
#             elif skip:
#                 skip -= 1
#             else:
#                 yield x

#     for x, y in itertools.zip_longest(F(S), F(T)):
#         print(x,y)



# backspaceCompare("take","fine")

n = 2

reversible_pairs = [
    ['0', '0'], ['1', '1'], 
    ['6', '9'], ['8', '8'], ['9', '6']
]

def generate_strobo_numbers(n, final_length):
    if n == 0:
        # 0-digit strobogrammatic number is an empty string.
        return [""]

    if n == 1:
        # 1-digit strobogrammatic numbers.
        return ["0", "1", "8"]

    prev_strobo_nums = generate_strobo_numbers(n - 2, final_length)
    curr_strobo_nums = []

    for prev_strobo_num in prev_strobo_nums:
        for pair in reversible_pairs:
            if pair[0] != '0' or n != final_length:
                curr_strobo_nums.append(pair[0] + prev_strobo_num + pair[1])

    return curr_strobo_nums
    
ans = generate_strobo_numbers(n, n)

print(ans)


