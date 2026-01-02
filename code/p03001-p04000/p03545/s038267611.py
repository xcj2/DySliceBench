import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
sys.setrecursionlimit(10**9)


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy


S = input()
A, B, C, D = map(int, [S[0], S[1], S[2], S[3]])
dump(A, B, C, D)
for op1, op2, op3 in it.product(['+', '-'], repeat=3):
    dump(op1, op2, op3)

    def f(op, a): return a * (1 if op == '+' else -1)
    ans = A + f(op1, B) + f(op2, C) + f(op3, D)
    dump(A, f(op1, B), f(op2, C), f(op3, D))
    if(ans == 7):
        print(str(A)+op1+str(B)+op2+str(C)+op3+str(D)+"=7")
        exit(0)
print("")
