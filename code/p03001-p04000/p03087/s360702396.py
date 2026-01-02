#!/usr/bin/env python3
import sys
# import random

# tc_1 = "".join([random.choice("ACGT") for x in range(100)])
# tc_q = sorted([random.choice(range(100)) for _ in range(2)])
# print(tc_1[tc_q[0]-1:tc_q[1]])
# print(tc_1[tc_q[0]-1:tc_q[1]].count("AC"))
# print(solve(1, 1, tc_1, [tc_q[0]], [tc_q[1]]))


def solve(N: int, Q: int, S: str, l: "List[int]", r: "List[int]"):
    # ACがある場所を記録する
    buf = None
    mem = []
    tot = 0
    for i, c in enumerate(S):
        if c == 'A':
            buf = 'A'
        elif buf == 'A' and c == 'C':
            tot += 1
            buf = None
        elif buf == 'A':
            buf = None
        mem.append(tot)
    # print(mem)
    for i in range(Q):
        print(mem[r[i]-1]-mem[l[i]-1])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, S, l, r)


if __name__ == '__main__':
    main()
