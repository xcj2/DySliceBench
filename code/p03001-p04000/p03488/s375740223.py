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

s = ns()
x,y = li()

command = s.split("T")

ud = set()
lr = set()

lr.add(len(command[0]))
ud.add(0)

for i, cm in enumerate(command[1:]):
    if i%2 == 1:
        new_lr = set()
        for element in lr:
            new_lr.add(element + len(cm))
            new_lr.add(element - len(cm))
            
        lr = new_lr
        
    else:
        new_ud = set()
        for element in ud:
            new_ud.add(element + len(cm))
            new_ud.add(element - len(cm))
            
        ud = new_ud

if (x in lr) and (y in ud):
    print("Yes")
else:
    print("No")