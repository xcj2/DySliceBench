import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n = ni()
ss = []
for _ in range(n):
    ss.append(lc())

alpha = [[0 for _ in range(n)] for _ in range(26)]


for i, s in enumerate(ss):
    c_set = set(list(s))
    for c in c_set:
        alpha[ord(c) - ord("a")][i] = s.count(c)

ans = ""
for i, a in enumerate(alpha):
    ans = ans + chr(ord("a")+i)*min(a)
    
print(ans)