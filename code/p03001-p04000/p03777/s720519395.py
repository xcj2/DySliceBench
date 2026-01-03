import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
from functools import partial, reduce
from operator import mul
prod = partial(reduce, mul)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

fibo = [1, 1]
for i in range(2, 9):
    fibo.append(fibo[i - 1] + fibo[i - 2])

def main():
    a, b = LS()
    if a == 'H':
        ans = b
    else:
        if b == 'H':
            ans = 'D'
        else:
            ans = 'H'
    return ans

print(main())