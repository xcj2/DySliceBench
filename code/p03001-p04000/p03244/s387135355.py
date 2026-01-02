#!/usr/bin/env python3
import sys


def solve(n: int, v: "List[int]"):
    counts = [{}, {}]
    for i in range(n):
        if v[i] in counts[i % 2]:
            counts[i % 2][v[i]] += 1
        else:
            counts[i % 2][v[i]] = 1
    l1 = list(counts[0].items()) + [(-1, 0)]
    l2 = list(counts[1].items()) + [(-1, 0)]
    l1.sort(reverse=True, key=lambda x: x[1])
    l2.sort(reverse=True, key=lambda x: x[1])
    #print(l1)
    #print(l2)
    tmp = 0
    if l1[0][0] == l2[0][0]:
        tmp = max(l1[0][1] + l2[1][1], l1[1][1] + l2[0][1])
    else:
        tmp = l1[0][1] + l2[0][1]
    ret = n - tmp
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    v = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, v)

if __name__ == '__main__':
    main()
