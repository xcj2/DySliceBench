#!/usr/bin/env python3
import sys
from itertools import groupby
from itertools import accumulate

def solve(N: int, K: int, S: str):
    group = groupby(S)

    one = []
    zero = []
    for key,value in group:
        if key == "1":
            one.append(len(list(value)))
        else:
            zero.append(len(list(value)))
    
    if len(zero) <= K:
        print(sum(one)+sum(zero))
        return
    
    # one がzeroより一つ多くなるように
    if len(one) == len(zero):
        if S[0] == "1":
            one.append(0)
        else:
            one = [0]+one
    elif len(zero) > len(one):
        one = [0]+one+[0]
    

    accum_zero = [0] + list(accumulate(zero))
    accum_one = [0] + list(accumulate(one))

    answer = 0
    for i in range(len(zero)-K+1):
        total = (accum_one[i+K+1]-accum_one[i]) + accum_zero[i+K]-accum_zero[i]
        answer = max(total,answer)
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = str(next(tokens))  # type: str
    solve(N, K, S)

if __name__ == '__main__':
    main()
