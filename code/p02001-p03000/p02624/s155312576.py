production = True

import sys, math, collections

def input(input_format = 0, multi = 0):

    if multi > 0: return [input(input_format) for i in range(multi)]
    else:
        next_line = sys.stdin.readline()[:-1]

        if input_format >= 10:
            use_list = False
            input_format = int(str(input_format)[-1])
        else: use_list = True

        if input_format == 0: formatted_input = [next_line]
        elif input_format == 1: formatted_input = list(map(int, next_line.split()))
        elif input_format == 2: formatted_input = list(map(float, next_line.split()))
        elif input_format == 3: formatted_input = list(next_line)
        elif input_format == 4: formatted_input = (lambda x: [x[0], list(map(int, x[1:]))])(next_line.split())
        elif input_format == 5: formatted_input = (lambda x: [x[0], list(map(float, x[1:]))])(next_line.split())
        elif input_format == 6: formatted_input = next_line.split()
        else: formatted_input = [next_line]

        return formatted_input if use_list else formatted_input[0]


def out(output_line, output_format = 0, newline = True):

    formatted_output = ""

    if output_format == 0: formatted_output = str(output_line)
    elif output_format == 1: formatted_output = " ".join(map(str, output_line))
    elif output_format == 2: formatted_output = "\n".join(map(str, output_line))

    print(formatted_output, end = "\n" if newline else "")


def log(*args):
    if not production:
        print("$$$", end = "")
        print(*args)

enum = enumerate

#
#   >>>>>>>>>>>>>>> START OF SOLUTION <<<<<<<<<<<<<<
#

p = []

def seive(n):
    global p

    p = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            p[j] += 1

def solve():

    n = input(11)

    seive(n)
    t = sum(map(lambda a: a[0] * a[1], enum(p)))

    out(t)
    
    return


#for i in range(input(11)): solve()
solve()

#
#   >>>>>>>>>>>>>>>> END OF SOLUTION <<<<<<<<<<<<<<<
#
