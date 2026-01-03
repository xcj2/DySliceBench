import sys
import heapq
import bisect
import itertools

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def LI_(): return([int(x)-1 for x in sys.stdin.readline().split()])
def S(): return(sys.stdin.readline()[:-1])
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

def Eratosthenes(N):
    r = [True]*(N+1)
    r[0] = False
    r[1] = False
    i = 2
    while i*i<=N:
        if r[i]: 
            j = i
            while i*j<=N:
                prime[i*j]=False
                j+=1
        i+=1
    return(r)

def main():
    N,M = LI()
    ll = [[] for _ in range(N)]
    dic = {}
    for i in range(N):
        KL = LI()
        ll[i] = [j-1 for j in KL[1:]]
        for l in KL[1:]:
            dic[l-1] = dic.get(l-1,[])
            dic[l-1].append(i)

    flagk = [True] * N
    flagl = {}
    for l in dic:
        flagl[l] = True

    que = [0]
    while que:
        k = que.pop()
        if flagk[k]:
            flagk[k] = False
            for l in ll[k]:
                if flagl[l]:
                    flagl[l] = False
                    for nxt in dic[l]:
                        if flagk[nxt]:
                            que.append(nxt)
    for x in flagk:
        if x:
            return("NO")
    return("YES")



if __name__ == "__main__":
    print(main())
