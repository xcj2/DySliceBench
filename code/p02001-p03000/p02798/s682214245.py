#!/usr/bin/env python3
import sys
from itertools import combinations

def solve(N: int, A: "List[int]", B: "List[int]"):
    answer = 10**10
 
    ## 奇数indexにくるものを決め打ち
    for c in combinations(range(N), N//2):
        even, odd= [], []
        
        for i in range(N):
            if i in c:
                odd.append((A[i] if i % 2 == 1 else B[i],i))
            else:
                even.append((A[i] if i % 2 == 0 else B[i],i))
    
        even.sort()
        odd.sort()
        t = []
        ind = []
        
        for i in range(N//2):
            t.append(even[i][0])
            t.append(odd[i][0])
            ind.append(even[i][1])
            ind.append(odd[i][1])
        else:
            if N%2 == 1:
                t.append(even[-1][0])
                ind.append(even[-1][1])
        
        if t != sorted(t):
            continue

        tentousuu = 0
        for i in range(N-1):
            for j in range(i+1,N):
                if ind[i] > ind[j]:
                    tentousuu += 1
        
        if answer > tentousuu:
            answer = tentousuu

    if answer == 10**10:
        print(-1)
    else:
        print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
