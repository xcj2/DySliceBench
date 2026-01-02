def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from collections import deque

N = INT()
Tree = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v, w = MI()
    Tree[u - 1].append((v - 1, w))
    Tree[v - 1].append((u - 1, w))
    
color = [0] * N
queue = deque([0])
visited = [False] * N

while queue:
    q = queue.popleft()
    visited[q] = True
    
    for t in Tree[q]:
        if not visited[t[0]]:
            if t[1] % 2 == 0:
                color[t[0]] = color[q]
                
            else:
                if color[q] == 0:
                    color[t[0]] = 1
                else:
                    color[t[0]] = 0
            
            queue.append(t[0])
        
for c in color:
    print(c)