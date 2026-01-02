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


def solve():

    n, m, k = input(1)
    a = input(1)
    b = input(1)


    ap = [0]
    bp = [0]

    for i in a:
        ap.append(ap[-1] + i)

    for i in b:
        bp.append(bp[-1] + i)


    log(ap, bp)

    pa = 0

    while pa < len(ap) and ap[pa] <= k:
        pa += 1

    m = pa - 1
    pb = 1

    c = k - ap[pa - 1]

    for i in range(pa - 1, -1, -1):
        while pb < len(bp) and bp[pb] <= c:
            m = max(pa - 1 + pb, m)
            pb += 1
        pa -= 1
        c += a[pa - 1]

    out(m)


        
    



    return


#for i in range(input(11)): solve()
solve()

#
#   >>>>>>>>>>>>>>>> END OF SOLUTION <<<<<<<<<<<<<<<
#
