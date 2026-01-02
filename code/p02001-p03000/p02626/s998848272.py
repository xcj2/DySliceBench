#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    def _to_bits(v):
        xb = []
        h = {}
        i = 0
        while v > 0:
            xb.append((2 ** i, v % 2))
            h[2 ** i] = v % 2
            v //= 2
            i += 1
        return xb, h
    xor = 0
    for i in range(2, N):
        xor ^= A[i]
    s = A[0] + A[1]
    #print(xor, s)
    rest = s - xor
    if rest < 0 or rest % 2 or (rest // 2) > A[0]:
        ret = -1
    else:
        ret = 0
        rest //= 2
        xb, xx = _to_bits(xor)
        rb, rr = _to_bits(rest)
        for k, v in rr.items():
            if v == 1 and k in xx and xx[k] == 1:
                ret = -1
                print(ret)
                return
        #print(xb)
        #print(rb)
        #print(rest)
        xb.reverse()
        tmp = rest
        for base, v in xb:
            #if v:
            #    print(base, v, tmp)
            if v and tmp + base < A[0]:
                tmp += base
        if tmp > 0:
            ret = A[0] - tmp
        else:
            ret = -1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
