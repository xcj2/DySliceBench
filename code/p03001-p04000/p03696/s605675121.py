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
s = lc()

left = 0
right = 0

cnt = 0

for si in s:
    if si == "(":
        right += 1
        
    elif si == ")":
        right -= 1
        
    if right < 0:
        left += 1
        right = 0
        
print("("*left + "".join(s) + ")"*right)