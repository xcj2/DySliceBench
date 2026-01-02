import sys
import time
sys.setrecursionlimit(20000)

def find(tree,x):
    (idx,weight) = tree[x]
    if(idx== -1):
        return x
    else:
        root_idx = find(tree,idx)
        tree[x] = (root_idx, tree[x][1] + tree[idx][1])
        return root_idx

def relate(tree,x,y,z):
    x_root_idx = find(tree,x)
    y_root_idx = find(tree,y)
    if(x_root_idx == y_root_idx):
        return False
    
    if (tree_rank[y_root_idx] < tree_rank[x_root_idx]):
        tree[y_root_idx] = (x_root_idx, z+tree[x][1]-tree[y][1])
    else:
        tree[x_root_idx] = (y_root_idx, -z-tree[x][1]+tree[y][1])
        if(tree_rank[x_root_idx]==tree_rank[y_root_idx]):
            tree_rank[y_root_idx] = tree_rank[y_root_idx] + 1
    #tree[x_root_idx] = (y_root_idx,z-tree[x_root_idx][1]+tree[y_root_idx][1])

def diff(tree,x,y):
    x_idx = find(tree,x)
    y_idx = find(tree,y)
    if not(x_idx == y_idx):
        return "?"
    return tree[y][1] - tree[x][1]

if __name__ == '__main__':
    N,query_num = map(int, input().split())
    weighted_union_find_tree = [(-1,0) for _ in range(N)]
    tree_rank = [0]*N
    for i in range(query_num):
        query = list(map(int,input().split()))
        if(query[0]==0):
            relate(weighted_union_find_tree,query[1],query[2],query[3])
            #print(weighted_union_find_tree)
            #print(tree_rank)
        elif(query[0]==1):
            res = diff(weighted_union_find_tree,query[1],query[2])
            print(res)


