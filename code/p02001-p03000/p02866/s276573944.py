#!/usr/bin/env python3
import sys
from collections import Counter
MOD = 998244353  # type: int

def solve(N: int, D: "List[int]"):
    if D[0] != 0:
        print(0)
        return 
    
    for i in range(1,N):
        if D[i]==0:
            print(0)
            return 

    ## 階層が飛んでるものを除く
    D.sort()
    counter = Counter(D).items()
    answer = 1
    prev_node_count = 1
    layer = 0
    for c in counter:
        if layer == c[0]: 
            answer*=prev_node_count**c[1]
            prev_node_count = c[1]
            layer+=1
        else:
            print(0)
            return 
    
    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, D)

if __name__ == '__main__':
    main()
