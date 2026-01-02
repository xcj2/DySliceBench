#!/usr/bin/env python3
import sys
import numpy as np

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, K: int, Q: int, A: "List[int]"):
    human = np.full(N, K)
    score = np.zeros(N)
    #print(human)
    for i in range(Q):
        #print("i =", i)
        # ind = np.ones(N, dtype=bool)
        # ind[A[i]-1] = False
        # human[ind] = human[ind] - 1
        # ind[A[i]-1] = True
        #human[A[i]-1] += 1
        #print('human =', human)
        score[A[i]-1] += 1

    human = human - Q + score

    #print(human)
    human2 = list(map(lambda x: YES if x > 0 else NO, human))
    print('\n'.join(human2))
    '''
    for j in range(N):
        #print(j, human[j])
        if human[j] > 0:
            print(YES)
        else:
            print(NO)
    '''
    return
    

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A)

if __name__ == '__main__':
    main()
