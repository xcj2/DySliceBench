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

n = ni()
a = list(li())

rate = [0]*9

for ai in a:
    if ai < 3200:
        rate[ai//400] = 1
    else:
        rate[8] += 1
        
if sum(rate[:-1]) == 0:
    print(1,rate[8])
    
else:
    print(sum(rate[:-1]), sum(rate[:-1])+rate[8])
    