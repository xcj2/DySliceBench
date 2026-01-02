import heapq
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()
    X = defaultdict(lambda: [])
    for i in range(N):
        a,b=mi()
        X[a].append(b)
    
    Y = []
    heapq.heapify(Y)
    ans = 0
    for x in reversed(range(M)):
        ok = M-x
        for x in X[ok]:
            heapq.heappush(Y,-1 * x)
        
        if Y:
            y = heapq.heappop(Y)
            y *= -1
            ans += y

    print(ans)


    


if __name__ == "__main__":
    main()