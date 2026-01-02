#!/usr/bin/env python3
import sys


def solve(N: int, M: int, s: "List[int]", c: "List[int]"):
    info = dict()
    info[1] = None
    info[2] = None
    info[3] = None
 
    for i in range(M):
        if info[s[i]] == None or info[s[i]] == c[i]:
            if s[i]==1 and c[i]==0 and N != 1:
                print(-1)
                return
            info[s[i]] = c[i]
        else:
            print(-1)
            return

    if (info[1] == 0 or info[1] == None) and N == 1:
        print(0)
        return
    num = ""
    for i in range(1,N+1):
        if info[i] == None:
            if i == 1:
                info[i] = 1
            else:
                info[i] = 0
        num += str(info[i])

    print(int(num))
    
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
