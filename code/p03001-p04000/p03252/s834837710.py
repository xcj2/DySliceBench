from sys import stderr
from functools import reduce
from collections import defaultdict as dd
from operator import add


def f():
    return [int(i) for i in input().split()]


def yes(n):
    print("Yes" if n else "No")


def debug(*x, sep=" ", end="\n"):
    for item in x:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)


s = input()
t = input()
pos_s = dd(list)
pos_t = dd(list)

for i, char in enumerate(s):
    pos_s[char].append(i)
for i, char in enumerate(t):
    pos_t[char].append(i)

for key_s, item_s in pos_s.items():
    for key_t, item_t in pos_t.items():
        if item_s == item_t:
            pos_s[key_s] = []
            pos_t[key_t] = []

yes(
    all([len(p) == 0 for p in pos_s.values()]) and all([len(p) == 0 for p in pos_t.values()]))
