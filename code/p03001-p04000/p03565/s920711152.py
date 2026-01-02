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

s = lc()
t = lc()

ans = "z"*50

match = False
for i in range(len(s)-1,-1,-1):
    if s[i] == '?' or s[i] == t[0]:
        for j, sij in enumerate(s[i:i+len(t)]):

            if sij != '?' and sij != t[j]:
                break

            if j == len(t)-1:
                match = True
                s[i:i+len(t)] = t[:]
    
    if match:
        break
                
if not match:
    print("UNRESTORABLE")
    
else:
    for i in range(len(s)):
        if s[i] == '?':
            s[i] = 'a'
            
    print("".join(s))