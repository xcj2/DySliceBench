import math
import sys

UNDEF=-1
sys.setrecursionlimit(1000010)
N = int(input())
# print(N)
V=[[UNDEF,UNDEF,[],[] ] for _ in range(N) ]      # Vertex
E=[[] for _ in range(N-1) ]    # Edge 

for i in range(N-1):
    (xa,xb) = map(int,input().split())
    # print(xa,xb)
    E[i]=[xa,xb]
    V[xb-1][0]=xa
    V[xb-1][1]=i+1
    V[xa-1][2].append(xb)
    V[xa-1][3].append(i+1)


# print("Edge:", E)
# print("Vertex:",V)

def root_v():
    global UNDEF
    global V
    for i in range(len(V)):
        if V[i][0] == UNDEF:
            return i+1
    return UNDEF

# print("Root Node:",root_v())

def max_degree(s):
    if V[s-1][0] != UNDEF: 
        degree=len(V[s-1][2]) + 1 # Node S 's degree for non root
    else:
        degree=len(V[s-1][2])     # Node S 's degree for root 

    for c in V[s-1][2]:
        degree = max ( degree, max_degree(c) ) 
    return degree

# print("Max Degree:", max_degree(root_v()))
print(max_degree(root_v()))

# Initialize 'color list' for edges
color=[UNDEF for _ in range(N-1)]

def put_colors(s):
    # print("put_color",s)
    global color 
    pcolor=UNDEF
    if V[s-1][1] != UNDEF:
        pcolor = color[V[s-1][1]-1]
    ic = 1
    for i in range(len(V[s-1][3])):
        if ic == pcolor:
            ic = ic + 1
        # print("put_color",s,i,V[s-1][3][i], ic )
        color[V[s-1][3][i]-1] = ic 
        put_colors(V[s-1][2][i])
        ic = ic + 1
    
put_colors(root_v())
for i in range(N-1):
    print(color[i])
