#!/usr/bin/env python3
import sys
def comb(n, k):
    k = min(n-k,k)
    ans = 1
    for i in range(1, k + 1):
        ans = (ans * (n + 1 - i) // i)
    return ans

def solve(N: int, P: int, A: "List[int]"):
    odd = 0
    even = 0

    for i in range(N):
        if A[i]&1:
            odd += 1
        else:
            even += 1
    
    all_pattern = 2**N
    odd_pattern = 0
    for o in range(1,odd+1):
        if o&1:
            odd_pattern += comb(odd,o)
    odd_pattern *= 2**even

    if P:
        print(odd_pattern)
    else:
        print(all_pattern-odd_pattern)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, A)

if __name__ == '__main__':
    main()
