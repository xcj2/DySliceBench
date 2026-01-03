def examD():
    H, W, N = LI()
    ab = set()
    for _ in range(N):
        a, b = list(map(int,input().split()))
        ab.add((a-1,b-1))
    check = set()
    for c in ab:
        for i in range(-1,2):
            for j in range(-1,2):
                if 1<=c[0]+i<H-1 and 1<=c[1]+j<W-1:
                    check.add((c[0]+i,c[1]+j))
#    print(check)
#    print(ab)
    ansC = [0]*10
    for c in check:
        cur = int(0)
        for i in range(-1,2):
            for j in range(-1,2):
                if (c[0]+i,c[1]+j) in ab:
                    cur += 1
        ansC[cur] +=1
    ansC[0] = (H-2)*(W-2)-sum(ansC)
    for v in ansC:
        print(v)


import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
