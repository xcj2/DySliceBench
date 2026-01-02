import sys

def input():
    return sys.stdin.readline()[:-1]
def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a<b:
        return a
    else:
        return b

from collections import deque

def BFS(vi,c,e_list,color_list):
        
    Q = deque([vi])
    color_list[vi] = c
    while len(Q)>0:
        v = Q.pop()
        for v1 in e_list[v]:
            if color_list[v1]==-1:
                color_list[v1]=c
                Q.appendleft(v1)



def main():
    H,W = list(map(int,input().split()))
    s1,s2 = list(map(int,input().split()))
    g1,g2 = list(map(int,input().split()))
    s1,s2 = s1-1,s2-1
    g1,g2 = g1-1,g2-1
    S = [input() for i in range(H)]

    def z(i,j):
        return i*W + j

    e_list = [[] for i in range(H*W)]

    for i in range(H):
        for j in range(W):
            if i!=H-1:
                if S[i][j]=="." and S[i+1][j]==".":
                    e_list[z(i,j)].append(z(i+1,j))
                    e_list[z(i+1,j)].append(z(i,j))
            if j!=W-1:
                if S[i][j]=="." and S[i][j+1]==".":
                    e_list[z(i,j)].append(z(i,j+1))
                    e_list[z(i,j+1)].append(z(i,j))

    color_list = [-1]*(H*W)
    c = 0


    for i in range(H*W):
        if S[i//W][i%W] == ".":
            if color_list[i]==-1:
                BFS(i,c,e_list,color_list)
                c+=1

    comp = max(color_list)+1
    e_list = [set([]) for i in range(comp)]


    for x in range(H*W):
        i,j = x//W,x%W
        if color_list[x]!=-1:
            for y in range(25):
                i1,j1 = y//5,y%5
                i2 = i1 + i - 2
                j2 = j1 + j - 2
                if 0<=i2 and i2<=H-1 and 0<=j2 and j2<=W-1:
                    if color_list[z(i2,j2)]!=-1 and color_list[z(i2,j2)]!=color_list[x]:
                        e_list[color_list[z(i2,j2)]].add(color_list[x])
                        e_list[color_list[x]].add(color_list[z(i2,j2)])

    vi = color_list[z(s1,s2)]  #change
    INF = float('inf')
    N = comp
    Q = deque([vi])

    checked_list = [False]*N
    checked_list[vi]=True

    min_path_list = [INF]*N #change
    min_path_list[vi] = 0
    #print(e_list)
    while len(Q)>0:
        v = Q.pop()
        for v1 in e_list[v]:
            if not checked_list[v1]:
                checked_list[v1]=True
                Q.appendleft(v1)
                min_path_list[v1]=min(min_path_list[v1],min_path_list[v]+1) #change
    if min_path_list[color_list[z(g1,g2)]]<=10**26:
        print(min_path_list[color_list[z(g1,g2)]])
    else:
        print(-1)

if __name__ == '__main__':
    main()

