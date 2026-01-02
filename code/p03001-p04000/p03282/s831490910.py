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
k = ni()

not1first_idx = len(s)
not1first = '1'

for i in range(len(s)):
    if s[i] != '1':
        not1first_idx = i
        not1first = s[i]
        break
        
        
if k >= not1first_idx+1:
    print(not1first)
    
else:
    print('1')