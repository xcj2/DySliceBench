from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n,p=MI()
    s=SI()
    if p==2 or p==5:
        ans=0
        for i,c in enumerate(s):
            if int(c)%p==0:ans+=i+1
        print(ans)
        exit()
    aa=[int(c) for c in s[::-1]]
    cc=[0]
    ten=1
    for a in aa:
        cc.append((cc[-1]+a*ten)%p)
        ten=ten*10%p
    cnt=Counter(cc)
    ans=0
    for v in cnt.values():
        ans+=v*(v-1)//2
    print(ans)

main()