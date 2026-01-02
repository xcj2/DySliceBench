import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(10000)

# Debug output
def chkprint(*args):
    names = {id(v):k for k,v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

# Binary converter
def to_bin(x):
    return bin(x)[2:]

# --------------------------------------------

dp = None
mintime = 9999

def f(current, time, draws):
    global mintime

    if time > mintime:
        return 999999

    if current == 0:
        mintime = min(mintime, time)
        return time

    i = 0
    while draws[i] > current:
        i += 1

    if i + 1 == len(draws):
        return f(current - draws[i], time + 1, draws)
    else:
        return min(f(current-draws[i], time+1, draws), f(current-draws[i+1], time+1, draws))

def main():
    N = int(input())
    draws = [59049, 46656, 7776, 6561, 1296, 729, 216, 81, 36, 9, 6, 1]

    print(f(N, 0, draws))

main()
