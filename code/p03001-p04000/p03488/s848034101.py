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

lr = len(command[0])
ud = 0

lr_cm = [len(cm) for cm in command[2::2]]
ud_cm = [len(cm) for cm in command[1::2]]

lr_cm.sort(reverse=True)
ud_cm.sort(reverse=True)

for cm in lr_cm:
    if lr > x:
        lr -= cm
    else:
        lr += cm
        
for cm in ud_cm:
    if ud > y:
        ud -= cm
    else:
        ud += cm
        
if lr == x and ud == y:
    print("Yes")
else:
    print("No")