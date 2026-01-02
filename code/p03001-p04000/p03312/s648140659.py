from collections import deque
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
    n=II()
    aa=LI()
    p=aa[0]
    q=aa[1]
    j=1
    dl=abs(p-q)
    k=3
    r=aa[2]
    s=sum(aa[3:])
    dr=abs(r-s)
    while abs(r-s+aa[k]*2)<dr:
        r+=aa[k]
        s-=aa[k]
        dr=abs(r-s)
        k+=1
    ans=max(p,q,r,s)-min(p,q,r,s)
    for i in range(3,n-1):
        q += aa[i - 1]
        dl = abs(p - q)
        while abs(p - q + aa[j] * 2) < dl:
            p += aa[j]
            q -= aa[j]
            dl = abs(p - q)
            j += 1

        r -= aa[i - 1]
        dr = abs(r - s)
        while abs(r-s+aa[k]*2)<dr:
            r+=aa[k]
            s-=aa[k]
            dr=abs(r-s)
            k+=1
        cur=max(p,q,r,s)-min(p,q,r,s)
        if cur<ans:ans=cur
    print(ans)

main()