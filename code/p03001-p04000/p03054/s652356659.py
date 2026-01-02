#!/usr/bin/env python3
import sys

YES = "YES"
NO = "NO"

def can_leave(n, p, S, T):
    min_p, max_p = p, p
    for i in range(len(S)):
        #print(min_p, max_p)
        if S[i] > 0:
            max_p += 1
        if S[i] < 0:
            min_p -= 1
        if max_p > n or min_p < 1:
            return False

        if min_p < n and T[i] > 0:
            min_p += 1
        if max_p > 1 and T[i] < 0:
            max_p -= 1
    return True


def solve(h: int, w: int, N: int, sr: int, sc: int, S: str, T: str):
    def make(st, n):
        ret_h, ret_w = [], []
        for i in range(n):
            if st[i] == 'U':
                ret_h.append(-1)
                ret_w.append(0)
            if st[i] == 'D':
                ret_h.append(1)
                ret_w.append(0)
            if st[i] == 'L':
                ret_w.append(-1)
                ret_h.append(0)
            if st[i] == 'R':
                ret_w.append(1)
                ret_h.append(0)
        return ret_h, ret_w

    hs, ws = make(S, N)
    ht, wt = make(T, N)
    h_can = can_leave(h, sr, hs, ht)
    w_can = can_leave(w, sc, ws, wt)
    #print(hs)
    #print(ht)
    #print(h_can)
    #print()
    #print(ws)
    #print(wt)
    #print(w_can)
    if  h_can and w_can:
        ret = YES
    else:
        ret = NO
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    s_r = int(next(tokens))  # type: int
    s_c = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(H, W, N, s_r, s_c, S, T)

if __name__ == '__main__':
    main()
