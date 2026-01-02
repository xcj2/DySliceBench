import bisect
import heapq
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()
    
    L,R,_L = [],[],[]
    for i in range(M):
        a,b=mi()
        L.append((a,i))
        R.append((b,i))
        _L.append(a)

    L.sort()
    R.sort()
    _L.sort()

    heapq.heapify(L)    
    heapq.heapify(R)

    l_e = 0
    ans = 0
    seen = set()
    while R:
        r,j = heapq.heappop(R)
        if j in seen: continue

        li = bisect.bisect_left(_L,r)
        if li > 0: li -= 1

        for i in range(l_e,li+1):
            seen.add(L[i][1])

        l_e = li
        ans += 1

    print(ans)




if __name__ == "__main__":
    main()