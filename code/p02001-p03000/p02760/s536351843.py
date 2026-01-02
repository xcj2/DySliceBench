#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    import numpy as np

    CARD = np.array(A,dtype=np.int8)

    for i in range(N):
        CARD[CARD==b[i]] = 0   

    CARD = CARD==0

    # 行が揃っているかチェック
    if np.all(CARD,axis=0).sum() > 0:
        print(YES)
        return
    
    if np.all(CARD,axis=1).sum()>0:
        print(YES)
        return
    
    if np.all(np.diag(CARD)):
        print(YES)
        return
    
    if np.all(np.diag(np.fliplr(CARD))):
        print(YES)
        return
    
    print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
