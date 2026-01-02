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

from collections import Counter

h,w = li()

cnt = Counter([])
for _ in range(h):
    tmp = lc()
    for c in tmp:
        cnt[c] += 1

exist = True

if h%2 == 0 and w%2 == 0:
    for key,value in cnt.items():
        if value%4 != 0:
            exist = False
            break
        
elif h%2 == 1 and w%2 == 1:
    odd = 0
    mod4_2 = 0
    for key,value in cnt.items():
        if value % 2 == 1:
            odd += 1
        elif value % 4 == 2:
            mod4_2 += 1
            
    if odd > 1:
        exist = False
    elif mod4_2 > (h+w-2)//2:
        exist = False
        
else:
    odmax = 0
    if h%2 == 0:
        odmax = h//2
    else:
        odmax = w//2
        
    
    mod4_2 = 0
    for key, value in cnt.items():
        if value%2 != 0:
            exist = False
            break
        elif value%4 == 2:
            mod4_2 +=1
            
    if mod4_2 > odmax:
        exist = False
        
        
if exist:
    print("Yes")
else:
    print("No")