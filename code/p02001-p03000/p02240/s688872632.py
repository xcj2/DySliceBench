# -*- coding: utf-8 -*-

def assignColor():
    for i in range(n):
        if C[i] == -1:
            #BFS(i)
            DFS(i)
            
#@profile
def BFS(start):
    global C
    Q = [start]
    C[start] = start

    while len(Q) != 0:
        u = Q.pop(0)
        v = [i for i in G[u] if C[i] == -1] # v := ??£??\???????????????????????¢?´¢??????????????????
        
        for i in v:
            Q.append(i)
            C[i] = C[start]

#@profile
def DFS(start):
    S = [start]
    C[start] = start
    while len(S) != 0:
        u = S.pop(0)
        for i in G[u]:
            if C[i] == -1:
                C[i] = start
                S.append(i)

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    G = [[] for i in range(n)]
    C = [-1]*n
    
    for i in range(m):
        s, t = list(map(int, input().split()))
        G[s].append(t)
        G[t].append(s)
    assignColor()
    q = int(input())
    for i in range(q):
        s, t = list(map(int, input().split()))
        if C[s] == C[t]:
            print("yes")
        else:
            print("no")
            