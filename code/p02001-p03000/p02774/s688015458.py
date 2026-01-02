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
    inf=10**18+1
    n,k=MI()
    aa=LI()
    pp=[]
    mm=[]
    zero=0
    for a in aa:
        if a>0:pp.append(a)
        elif a<0:mm.append(a)
        else:zero+=1
    pp.sort()
    mm.sort()
    cm=len(mm)*len(pp)
    cz=zero*(zero-1)//2+zero*(n-zero)

    def ok1(c):
        i=0
        cnt=0
        for m in mm:
            while i<len(pp) and m*pp[i]>=c:i+=1
            if i==len(pp):break
            cnt+=len(pp)-i
        return cnt<k

    def ok2(c):
        cnt=0
        j=len(mm)-1
        for i,m in enumerate(mm):
            while j>i and m*mm[j]>=c:j-=1
            if i>=j:break
            cnt+=j-i
        j=len(pp)-1
        for i,p in enumerate(pp):
            while j>i and p*pp[j]>=c:j-=1
            if i>=j:break
            cnt+=j-i
        return cnt<k

    # 答えが負
    if k<=cm:
        l=-inf
        r=inf
        while l+1<r:
            c=(l+r)//2
            if ok1(c):l=c
            else:r=c
    # 答えが0
    elif k<=cm+cz:
        print(0)
        exit()
    # 答えが正
    else:
        mm.reverse()
        k-=cm+cz
        l=-inf
        r=inf
        while l+1<r:
            c=(l+r)//2
            if ok2(c):l=c
            else:r=c
    print(l)

main()