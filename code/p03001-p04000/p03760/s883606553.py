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

o = lc()
e = lc()

ans = []

if len(o)-len(e) == 0:
    for i in range(len(o)):
        ans.append(o[i])
        ans.append(e[i])
        
else:
    for i in range(len(e)):
        ans.append(o[i])
        ans.append(e[i])
        
    ans.append(o[i+1])


print("".join(ans))