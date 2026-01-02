# -*- coding: utf-8 -*-

def assignColor():
    C = [-1 for i in range(n)]
    for i in range(n):
        if C[i] == -1:
            C = BFS(G, i, C)
    return C

#@profile
def BFS(G, start, C):
    n = len(G)
    Q = [start]
    C[start] = start

    while len(Q) != 0:
        u = Q.pop(0)
        v = [i for i in G[u] if C[i] == -1] # v := ??£??\???????????????????????¢?´¢??????????????????
        
        for i in v:
            Q.append(i)
            C[i] = C[start]
    
    return C

def main():
    
    for i in range(m):
        s, t = list(map(int, input().split()))
        G[s].append(t)
        G[t].append(s)

    C = assignColor()
        
    q = int(input())
    
    for i in range(q):
        s, t = list(map(int, input().split()))
        if C[s] == C[t]:
            print("yes")
        else:
            print("no")
            
if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    G = [[] for i in range(n)]

    main()    