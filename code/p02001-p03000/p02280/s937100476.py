def det_par_sib_deg(nodes):
    n = len(nodes)
    parent = [-1] * n
    sibling = [-1] * n
    degree = [0] * n
    
    for i in range(n):
        p = nodes[i][0]
        l = nodes[i][1]
        r = nodes[i][2]
        if l==-1 and r==-1:
            degree[i] = 0
        elif l!=-1 and r==-1:
            parent[l] = p
            degree[i] = 1
        elif l==-1 and r!=-1:
            parent[r] = p
            degree[i] = 1
        else:
            parent[l] = parent[r] = p
            sibling[l] = r
            sibling[r] = l
            degree[i] = 2
    
    return parent, sibling, degree

def get_root(parent):
    n = len(parent)
    for i in range(n):
        if parent[i]==-1:
            return i

def det_types(root,nodes,degree):
    n = len(nodes)
    types = [""] * n
    for i in range(n):
        if degree[i]==0:
            types[i] = "leaf"
        else:
            types[i] = "internal node"
    types[root] = "root"
    return types

def get_child(num,nodes,degree):
    deg = degree[num]
    if deg==2:
        return deg, [nodes[num][1], nodes[num][2]]
    if deg==1:
        if nodes[num][1]==-1:
            return deg, [nodes[num][2]]
        else:
            return deg, [nodes[num][1]]
    if deg==0:
        return deg, []

def get_leaves(nodes,types):
    n = len(nodes)
    leaves = []
    for i in range(n):
        if types[i]=="leaf":
            leaves.append(i)
    return leaves

def det_height_depth(root,nodes,parent,types):
    n = len(nodes)
    height = [0] * n
    depth = [0] * n
    
    leaves = get_leaves(nodes,types)    
    for leaf in leaves:
        branch = [leaf]
        h = 1
        p = parent[leaf]
        while p!=-1:
            branch.append(p)
            if h>height[p]:
                height[p] = h
            p = parent[p]
            h += 1
        for i,node in enumerate(branch):
            depth[node] = (h-1) - i
        
    return height, depth

# def det_depth(root,nodes,parent,types,height):
#     n = len(nodes)
#     depth = [0] * n
    
#     leaves = get_leaves(nodes,types)
    
#     for leaf in leaves:
#         h = 1
#         p = parent[leaf]
#         branch = [leaf, p]
#         while p!=-1:
#             p = parent[p]
#             branch.append(p)
#             h += 1
#         for node in branch:
#             depth[node] = (h - 1) - height[node]
        
#     return depth

def print_res(n, nodes):
    parent, sibling, degree = det_par_sib_deg(nodes)
    root = get_root(parent)
    types = det_types(root,nodes,degree)
    height, depth = det_height_depth(root,nodes,parent,types)
    for i in range(n):
        num = nodes[i][0]        
        print("node " + str(num) + \
              ": parent = " + str(parent[i]) + \
              ", sibling = " + str(sibling[i]) + \
              ", degree = " + str(degree[i]) + \
              ", depth = " + str(depth[i]) + \
              ", height = " + str(height[i]) + \
              ", " + types[i] )

if __name__ == "__main__":
    n = int(input())
    nodes = [[]] * n
    for i in range(n):
        node = list(map(int, input().split()))
        nodes[node[0]] = node
    print_res(n,nodes)
