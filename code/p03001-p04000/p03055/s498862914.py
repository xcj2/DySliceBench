from collections import deque
from heapq import heappush,heappop
import re
def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

def getDeci(tree):
    def saiki(v):
        root = [0,v,-1]
        cur = None
        qu = deque()
        qu.append(root)
        while len(qu)!=0:
            cur = qu.popleft()
            for e in tree[cur[1]]:
                if e ==cur[2]:
                    continue
                qu.append([cur[0]+1,e,cur[1]])
        return cur
    leaf = saiki(0)
    ans = saiki(leaf[1])
    return ans

    
N = int_raw()
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = ints_raw()
    a = a-1
    b = b-1
    tree[a].append(b)
    tree[b].append(a)



def main():
    ans = getDeci(tree)
    if (ans[0]+2)%3==0:
        return "Second"
    else:
        return "First"

print(main())
