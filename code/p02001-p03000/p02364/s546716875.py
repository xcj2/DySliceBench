num_v,num_e=input().split()

edges=[]
verticies=[]

for i in range(int(num_e)):
    v,u,w=input().split()
    e=(v,u,int(w))
    edges.append(e)


for v in range(int(num_v)):
    v=str(v)
    verticies.append(v)

#for i in range(num_e):
#    e=(e_list[i*3],e_list[i*3+1],int(e_list[i*3+2]))
#    edges.append(e)

graph={
    'verticies':verticies,
    'edges':edges
}


parent={}
g_len={}

def group(v):
    parent[v]=v
    g_len[v]=0

def my_parent(v):
    if parent[v]!=v:
        parent[v]=my_parent(parent[v])
    return parent[v]
    
    
def union(v, u): 
    g_v=my_parent(v)
    g_u=my_parent(u)
    if g_v != g_u:
        if g_len[g_v] >= g_len[g_u]:
            parent[g_u]=parent[g_v]
            g_len[g_v] +=1
        else:
            parent[g_v]=parent[g_u]
            g_len[g_u] +=1
            

def kruskal(graph):
    g_list=[]
    sum_w=0
    
    for v in graph['verticies']:
        group(v)
        
    edges=graph['edges']
    edges.sort(key=lambda edges:edges[2])
    
    for edge in edges:
        v, u, weight =edge
        
        if my_parent(v) != my_parent(u):
            union(v,u)
            g_list.append(edge)
            sum_w=sum_w + weight
            
    return sum_w
    

print(kruskal(graph))
