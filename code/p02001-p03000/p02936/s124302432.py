import sys
import heapq
import bisect

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(sys.stdin.readline()[:-1])
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

def main():
    N,Q = LI()
    node=[[] for _ in range(N)]
    flag = [True for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        node[a-1].append(b-1)
        node[b-1].append(a-1)

    counter = [0] * N
    for _ in range(Q):
        p,x = LI()
        counter[p-1] += x

    cur = [[0,0]]
    while cur:
        nxt = []
        for a,c in cur:
            flag[a]=False
            counter[a]+=c
            for b in node[a]:
                if flag[b]:
                    nxt.append([b,counter[a]])
        cur = [x for x in nxt]

    r = [counter[i] for i in range(N)]

    return(" ".join(map(str,r)))

if __name__ == "__main__":
    print(main())
