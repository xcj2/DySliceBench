import sys
from collections import deque
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

deq=deque(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

K=II()
for i in range(K-1):
    v = deq.popleft()
    last = int(v[-1])
    if last == 0:
        deq.append(v + "0")
        deq.append(v + "1")
    elif last == 9:
        deq.append(v + "8")
        deq.append(v + "9")
    else:
        deq.append("{}{}".format(v, last-1))
        deq.append("{}{}".format(v, last))
        deq.append("{}{}".format(v, last+1))

print(deq.popleft())
