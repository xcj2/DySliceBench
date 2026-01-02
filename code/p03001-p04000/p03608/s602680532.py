import sys
import heapq
import bisect
import itertools

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
    N,M,R = LI()
    r = LI()
    node = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = LI()
        node[a-1].append([b-1,c])
        node[b-1].append([a-1,c])

    dic = {}
    for x in r:
        dic_part = {}
        for y in r:
            dic_part[y-1] = 0
        dic[x-1] = dic_part

    for x in r:
        ques = []
        flag = [True] * len(node)
        heapq.heappush(ques,[0,x-1])
        while ques:
            dist,crt = heapq.heappop(ques)
            if flag[crt]:
                flag[crt] = False
                if (crt+1) in r:
                    dic[x-1][crt] = dist
                    dic[crt][x-1] = dist
                for nxt,nxt_dist in node[crt]:
                    if flag[nxt]:
                        heapq.heappush(ques,[dist+nxt_dist,nxt])
    ans = 10**11
    for tr in itertools.permutations(r):
        tans = 0
        for i in range(len(tr)-1):
            tans += dic[tr[i]-1][tr[i+1]-1]
        ans = min(ans,tans)
    return(ans)

if __name__ == "__main__":
    print(main())
