#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def solve(N: int, A: "List[int]", B: "List[int]"):
    s = {}
    for i in range(N):
        if A[i] == 0 and B[i] == 0:
            a, b = 0, 0
        elif A[i] == 0:
            a, b = 0, 1
        elif B[i] == 0:
            a, b = 1, 0
        else:
            g = gcd(A[i], B[i])
            a, b = A[i] // g, B[i] // g
        k = (a, b)
        if not k in s:
            s[k] = 0
        s[k] += 1
    count = 0
    checked = set()
    cums = []
    #print(s)
    for (a, b), cnt in s.items():
        if (a, b) in checked:
            continue
        checked.add((a, b))
        tmp = 0
        if a == 0 and b == 0:
            count += cnt
            #cum = cnt + 1
            #cums.append(cum)
            #count += cnt + tmp
            continue
        if (-b, a) in s and (-b, a) not in checked:
            tmp += s[(-b, a)]
            checked.add((-b, a))
        if (b, -a) in s and (b, -a) not in checked:
            tmp += s[(b, -a)]
            checked.add((b, -a))
        if tmp > 0:
            cum = pow(2, cnt, MOD) + pow(2, tmp, MOD) - 1
            cum %= MOD
            cums.append(cum)
            count += cnt + tmp
    #print(cums, count)
    ret = pow(2, (N - count), MOD)
    for cum in cums:
        ret *= cum
        ret %= MOD
    if (0, 0) in s:
        ret += s[(0, 0)]
    ret -= 1
    ret %= MOD
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
