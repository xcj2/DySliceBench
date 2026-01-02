#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import collections


def simple_count(S, changed=False):
    count = 0
    for i in range(len(S) - 1):
        if changed:
            changed = False
        else:
            if S[i] == S[i + 1]:
                changed = True
                count += 1
    return count, changed


def solve(S, K):
    if K == 1:
        return simple_count(S)[0]
    if S[0] != S[-1]:
        return simple_count(S)[0] * K
    else:
        count2, changed = simple_count(S * 2)
        # print(count2, changed)
        if changed:
            return count2 * (K // 2) + simple_count(S, changed=False)[0] * (K % 2)
        else:
            return (count2) * (K // 2) + 1 * (K // 2-1 + K % 2) + simple_count(S, changed=True)[0] * (K % 2)
        # return simple_count(S + S[0])[0] * K


def test(S, K):
    SS = "".join([c for c in reversed(S)])
    # assert solve(S, K) == solve(SS, K), "{} {} = {} {}".format(S, SS, solve(S, K), solve(SS, K))
    assert solve(S, K) == simple_count(S * K)[0], "{} {} = {} {}".format(S, K, solve(S, K), simple_count(S * K)[0])


assert solve("cooooooooonteeeeeeeeeest", 999993333) == 8999939997
assert solve("aqqq", 2) == simple_count("aqqq" * 2)[0]
test("qq", 81)
# print(solve("qqq", 2), simple_count("qqq" * 2)[0])
assert solve("qqq", 2) == simple_count("qqq" * 2)[0]
# print(solve("qqq", 3), simple_count("qqq" * 3)[0])
assert solve("qqq", 3) == simple_count("qqq" * 3)[0]
assert solve("issii", 2) == simple_count("issii" * 2)[0]

test("iqi", 3)
test("iqqqqiiii", 1)
test("iqi", 2)
test("iqqqqiiii", 2)
test("iqii", 3)
test("iqii", 4)
test("iqqqqiiii", 6)
test("iqqqqiiii", 7)
test("qqqqqiiiii", 7)
test("q", 7)
test("qiq", 1)
test("qiq", 3)
test("qiq", 7)
test("qqq", 7)
test("qq", 7)
test("abcdef", 7)
test("qbbbq", 7)
test("qqqq", 7)
test("qqqqq", 7)

S = sys.stdin.readline().rstrip()
K, = map(int, sys.stdin.readline().rstrip().split(" "))
SS = "".join([c for c in reversed(S)])
print(min(solve(S, K), solve(SS, K)))

exit(0)
