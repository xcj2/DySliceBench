#!/usr/bin/env python3
import sys
from itertools import accumulate

def solve(N: int, K: int, x: "List[int]"):
    minus = []
    plus = []
    answer = 10**9
    for i in range(N):
        if x[i] >= 0:
            plus.append(x[i])
        else:
            minus.append(abs(x[i]))
    minus = minus[::-1]

    for plus_count in range(0,K+1):
        minus_count = K- plus_count

    
        if 0 <= plus_count <= len(plus) and 0 <= minus_count <= len(minus):
            if plus_count == 0:
                answer = min(answer,minus[minus_count-1])
            elif minus_count ==0:
                answer = min(answer,plus[plus_count-1])
            else:
                answer = min(answer,plus[plus_count-1]+minus[minus_count-1]*2,plus[plus_count-1]*2+minus[minus_count-1])   

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
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, x)

if __name__ == '__main__':
    main()
