#! /usr/bin/env python3
import itertools
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(N: int, P: "List[int]", Q: "List[int]"):
    X = list(range(1,N+1))
    R = []
    for r in itertools.permutations(X,N):
        R.append(int("".join(list(map(str,r)))))
        
    R.sort() 
    P = int("".join(P))
    Q = int("".join(Q))
    a,b = 0,0
    for i,r in enumerate(R):
        if r == P:
            a = i
        if r == Q:
            b = i

    print(abs(a-b))
    


    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [str(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [str(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)



if __name__ == "__main__":
    main()
