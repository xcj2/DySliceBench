import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

stot = dict()
ttos = dict()

s = lc()
t = lc()

ans = True

for si,ti in zip(s,t):
    if not si in stot.keys():
        stot.update({si: ti})
    elif stot[si] != ti:
        ans = False
        break
        
    if not ti in ttos.keys():
        ttos.update({ti: si})
    elif ttos[ti] != si:
        ans = False
        break
    
print('Yes') if ans else print('No')