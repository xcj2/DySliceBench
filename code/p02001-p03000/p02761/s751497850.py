#!/usr/bin/env python3
import sys


def solve(N: int, M: int, s: "List[int]", c: "List[int]"):

    G = [-1]*N

    for i in range(M):
        if G[s[i]-1] != -1 and G[s[i]-1] != c[i] :
            print(-1)
            sys.exit()
        elif s[i] == 1 and c[i] == 0 and N != 1:
            print(-1)
            sys.exit()
        else:
            G[s[i]-1] = c[i]


    for j in range(N-1):
        if G[j+1] == -1:
            G[j+1] = 0


    if G[0] == -1 and N >= 2:
        G[0] = 1
    
    if G[0] == -1 and N == 1:
        G[0] = 0
         

    G = [str(n) for n in G]

    num = ''.join(G)

    print(num)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, s, c)

if __name__ == '__main__':
    main()
