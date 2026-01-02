import sys
import math

def propare():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))

    solve(N)

def solve(N: int):
    # Symmetry, a<=b, a<=math.sqrt(N)
    N_max = min(N, 1000000000000)
    a_max = int(math.sqrt(N_max))
    tmp_list = []
    for a in range(1, a_max+1):
        if N%a == 0:
            b = int(N/a)
            tmp_list.append((a, b))

    if tmp_list:
        answer = tmp_list[0][0] + tmp_list[0][1]

    for i_tp in tmp_list:
        tmp = i_tp[0] + i_tp[1]

        if tmp < answer:
            answer = tmp

    print(answer - 2)
    return

 
if __name__ == "__main__":
    propare()