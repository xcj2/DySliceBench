import sys
input = sys.stdin.buffer.readline
from collections import defaultdict
import heapq

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    d = defaultdict(list)
        
    I = [i for i in range(N)]
    rank = [1 for _ in range(N)]
    def root(a):
        if I[a] == a:
            return a
        else:
            I[a] = root(I[a])
            return I[a]
            
    def unite(a,b):
        pa,pb = root(a),root(b)
        ra,rb = rank[a],rank[b]
        if ra > rb:
            I[pb] = pa
        else:
            I[pa] = pb
            if ra == rb:
                rank[pb] += 1
    
    for _ in range(M):
        x,y = map(int,input().split())
        unite(x,y)
        parent = root(x)
    
    for i,num in enumerate(I):
        parent = root(num)
        heapq.heappush(d[parent],a[i])
        
    if M == N-1:
        print(0)
        exit()
    elif N < 2*(N-M-1):
        print("Impossible")
        exit()

    l = len(d.keys())
    ans = 0
    rest = []
    for use in d.values():
        ans += heapq.heappop(use)
        rest.extend(use)

    remain = 2*(N-M-1)-l
    rest.sort()
    ans += sum(rest[:remain])
    
    print(ans)
    
if __name__ == "__main__":
    main()
