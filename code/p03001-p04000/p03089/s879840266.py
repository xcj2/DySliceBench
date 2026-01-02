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

n = ni()
b = list(li())

ans = []
exist = True

res = n

while res > 0:
    cur = -1
    for i in range(len(b)):
        if b[i] == i+1:
            cur = i
            
    if cur == -1:
        exist = False
        break
    else:
        b = b[:cur] + b[cur+1:]
        ans.append(cur+1)
        
    res -= 1

if not exist:
    print(-1)
else:
    for ansi in ans[::-1]:
        print(ansi)