#!/usr/bin/env python3
import sys

def solve(H: int, W: int, S: "List[str]"):
    tab = [0 for i in range(H*W)]
    for i in range(W):
        acc0, acc1 = 0, 0
        for j in range(H):
            j2 = H-1-j
            tab[W*j+i] += acc0
            tab[W*j2+i] += acc1
            acc0 = 0 if S[j][i] == "#" else acc0+1
            acc1 = 0 if S[j2][i] == "#" else acc1+1
    for j in range(H):
        acc2, acc3 = 0, 0
        for i in range(W):
            i2 = W-1-i
            tab[W*j+i] += acc2
            tab[W*j+i2] += acc3
            if S[j][i] == "#":
                tab[W*j+i] = -10**10
            else:
                tab[W*j+i] += 1
            acc2 = 0 if S[j][i] == "#" else acc2+1
            acc3 = 0 if S[j][i2] == "#" else acc3+1
    
    print(max(max(tab), 0))

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
