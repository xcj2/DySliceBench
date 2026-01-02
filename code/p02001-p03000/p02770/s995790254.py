#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(k: int, q: int, d: "List[int]", n: "List[int]", x: "List[int]", m: "List[int]"):

    for i in range(q):
        dmod = [v % m[i] for v in d]
        zero = 0
        c, p = divmod(n[i]-1, k)
        last = x[i]
        # print("dmod", dmod)
        # print("c, p", (c, p))
        for j in range(k):
            if j < p:
                last += (c+1)*dmod[j]
                if dmod[j] == 0:
                    zero += c+1
            else:
                last += c*dmod[j]
                if dmod[j] == 0:
                    zero += c
        print(n[i]-1-(zero + (last//m[i] - x[i]//m[i])))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    k = int(next(tokens))  # type: int
    q = int(next(tokens))  # type: int
    d = [int(next(tokens)) for _ in range(k - 1 - 0 + 1)]  # type: "List[int]"
    n = [int()] * (q)  # type: "List[int]"
    x = [int()] * (q)  # type: "List[int]"
    m = [int()] * (q)  # type: "List[int]"
    for i in range(q):
        n[i] = int(next(tokens))
        x[i] = int(next(tokens))
        m[i] = int(next(tokens))
    solve(k, q, d, n, x, m)


if __name__ == '__main__':
    main()
