import sys
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
n, m = MI()
lr = [LI() for _ in range(m)]
l = lr[0][0]
r = lr[0][1]
for i in range(1, m):
    if lr[i][0] < l and lr[i][1] < l:
        print(0)
        exit()
    if r < lr[i][0] and r < lr[i][1]: 
        print(0)
        exit()
    if l <= lr[i][0] <= r:
        l = lr[i][0] 
    if l <= lr[i][1] <= r:
        r = lr[i][1]
print(r - l + 1)
