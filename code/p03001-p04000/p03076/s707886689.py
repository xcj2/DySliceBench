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

abcde = [ni() for _ in range(5)]
wait = []
ans = 0

for i in abcde:
    if i%10 == 0:
        ans += i
        wait.append(0)
    else:
        wait.append(10 - i%10)
        ans += 10 * (i//10 + 1)
    
wait.sort()
print(ans - wait[-1])

    