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

h,w,k = li()
MOD = 10**9+7

cnt = [[0 for _ in range(w)] for _ in range(h+1)]
cnt[0][0] = 1

nex_list = []
for i in range(1<<(w-1)):
    if not "11" in bin(i)[2:]:
        nex_list.append(i)
        
for hi in range(1,h+1):
    for bit in nex_list:
        changed = [0]*w

        for i, b in enumerate(bin(bit)[2:].zfill(w-1)):
            
            if b == "1":
                cnt[hi][i] += cnt[hi-1][i+1]
                cnt[hi][i+1] += cnt[hi-1][i]
                changed[i] = 1
                changed[i+1] = 1
        for j,c in enumerate(changed):
            if c == 0:
                cnt[hi][j] += cnt[hi-1][j]
                
    for wj in range(w):
        cnt[hi][wj] %= MOD
        
print(cnt[h][k-1])
        