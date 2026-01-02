from collections import Counter,defaultdict,deque
import sys
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
    
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])


def main():
    n = inp()
    g = [[] for _ in range(n)]
    color = [0 for _ in range(n)]
    did = [0 for _ in range(n)]
    dic = defaultdict(str)
    p = []
    for _ in range(n-1):
        a,b = inpm()
        a -= 1
        b -= 1
        g[b].append(a)
        g[a].append(b)
        if a<b:
            a,b = b,a
        key = [str(a)]
        key.append(' ')
        key.append(str(b))
        key = ''.join(key)
        p.append(key)
        dic[key] = 1
    que = deque([])
    did[0]=1
    que.append(0)
    ans = 0
    while que:
        start = que.pop()
        go = g[start]
        c = 1
        for i in range(len(go)):
            t = go[i]
            if did[t]:
                continue
            else:
                if c == color[start]:
                    c += 1
                did[t] = 1
                que.append(t)
                color[t] = c
                ans = max(ans,c)
                key = []
                x = start
                y = t
                if x<y:
                    x,y = y,x
                key.append(str(x))
                key.append(' ')
                key.append(str(y))
                key = ''.join(key)
                dic[key] = c
                c += 1
    print(ans)
    for i in range(n-1):
        key = p[i]
        print(dic[key])

if __name__ == "__main__":
    main()