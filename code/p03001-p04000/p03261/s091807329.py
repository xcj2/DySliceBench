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

word = []
words = []
for _ in range(n):
    words.append(lc())
    
ok = True
for i in range(n-1):
    if words[i][-1] != words[i+1][0]:
        ok = False
        
for i in range(n):
    for j in range(i+1,n):
        if words[i] == words[j]:
            ok = False

if ok:
    print("Yes")
else:
    print("No")