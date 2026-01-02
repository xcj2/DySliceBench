import sys
import time
sys.setrecursionlimit(20000)

def find(tree,x):
    idx = tree[x]
    if(idx== x):
        return x
    else:
        root_idx = find(tree,tree[idx])
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

def unite(tree,x,y):
    x_root_idx = find(tree,x)
    y_root_idx = find(tree,y)

    if not (x_root_idx == y_root_idx):
        if(tree_rank[x_root_idx] < tree_rank[y_root_idx]):
            tree[x_root_idx] = y_root_idx
        else:
            tree[y_root_idx] = x_root_idx
            if(tree_rank[x_root_idx] == tree_rank[y_root_idx]):
                tree_rank[x_root_idx] = tree_rank[x_root_idx] + 1

def same(tree,x,y):
    x_root_idx = find(tree,x)
    y_root_idx = find(tree,y)
    if(x_root_idx == y_root_idx):
        return True
    else:
        return False

if __name__ == '__main__':
    #start = time.time()
    N,query_num = map(int, input().split())
    union_find_tree = [i for i in range(N)]
    tree_rank = [0]*N
    for i in range(query_num):
        operate,x,y = map(int, input().split())
        if(operate==0):
            unite(union_find_tree,x,y)
        if(operate==1):
            res = same(union_find_tree,x,y)
            if(res):
                print("1")
            else:
                print("0")
    #elapsed_time = time.time() - start
    #print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

