#!/usr/bin/env python3
import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_ok(n):
    if n % 2 == 1 and is_prime(n) and is_prime((n + 1) // 2):
        return True
    return False

def solve(Q: int, l: "List[int]", r: "List[int]"):
    N = 100000
    tmp = [0] * (N + 2)
    tmp[0] = 0
    tmp[1] = 0
    for i in range(1, N + 1):
        tmp[i + 1] = tmp[i]
        if is_ok(i):
            #print(i)
            tmp[i + 1] += 1
    #print(tmp[:10])
    for q in range(Q):
        ret = tmp[r[q] + 1] - tmp[l[q]]
        print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]" 
    r = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(Q, l, r)

if __name__ == '__main__':
    main()
