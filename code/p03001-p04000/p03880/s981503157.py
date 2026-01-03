import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def find_last_one(n: int):
    nbin = bin(n)[2:]
    return 29 - nbin[::-1].index('1')

# 入力
n = ni()
a = [ni() for _ in range(n)]

# aiについて、1のbitともっとも下の1のbit記録
onebit = [0]*30
lastonebit = [0]*30

for ai in a:
    lastonebit[find_last_one(ai)] += 1
    for mask in range(30):
        if ai & (1<<mask):
            onebit[29-mask] += 1

# 上位桁から確定させていく
ans = 0
for digit in range(30):
    if onebit[digit] % 2 == 0:
        continue
    
    elif lastonebit[digit] == 0:
        ans = -1
        break
    
    else:
        ans += 1
        onebit[digit] -= 1
        for d in range(digit+1, 30):
            onebit[d] += 1
            
print(ans)
            