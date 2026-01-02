# -*- coding: utf-8 -*-
import sys
import math
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

# BEGIN CUT HERE
import collections
class Devisor(int):
    def __init__(self, n: int):
        self.val = n

    def isprime(self):
        if self.val <= 1:
            return 0
        for i in range(2, int(math.sqrt(self.val)) + 1):
            if self.val % i == 0:
                return 0
        return 1

    def factorize(self):
        res = collections.defaultdict(int)
        n = self.val
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
                res[i] += 1
            i += 1
        if n != 1:
            res[n] += 1
        return res

    def divisor(self):
        n = self.val
        ret = list()
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                ret.append(i)
                ret.append(n // i) if i * i != n else None
        return ret

# END CUT HERE

def main():
    N = ii()
    d = Devisor(N).divisor()
    m = 10**18
    for x in d:
        if x + N // x < m:
            m = x + N // x
    print(m - 2)
    return


if __name__ == '__main__':
    main()
