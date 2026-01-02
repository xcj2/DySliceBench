import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

s = lc()

alpha = [chr(i) for i in range(ord("a"), ord("z")+1)]
lst = [0]*26

for i,a in enumerate(alpha):
    lst[i] = s.count(a)
    
exist = False
for i in range(26):
    if lst[i] == 0:
        print(alpha[i])
        exist = True
        break
        
if not exist:
    print("None")