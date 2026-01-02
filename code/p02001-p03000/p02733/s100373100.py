import numpy as np
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
    popcnt=lambda bit:bin(bit).count("1")
    h,w,k=MI()
    aa=[[0]+[int(c) for c in SI()] for _ in range(h)]
    aa=np.array(aa,dtype="i8")
    for i in range(h):
        aa[i]=np.cumsum(aa[i])
    #print(aa)
    ans=h+w
    for bit in range(1<<(h-1)):
        s=aa[0].copy()
        sn=popcnt(bit)+1
        ss=np.zeros((sn,w+1),dtype="i8")
        si=0
        for i in range(1,h):
            if bit>>(i-1)&1:
                ss[si]=s
                s=aa[i].copy()
                si+=1
            else:s+=aa[i]
        ss[si]=s
        #print(bin(bit))
        #print(ss)
        #print()
        cnt=popcnt(bit)-1
        j=0
        while j<w:
            cnt+=1
            mn=10**9
            for i in range(sn):
                nj=np.searchsorted(ss[i],ss[i][j]+k,side="right")-1
                mn=min(mn,nj)
            if mn==j:
                cnt=10**9
                break
            j=mn
        ans=min(ans,cnt)
    print(ans)

main()