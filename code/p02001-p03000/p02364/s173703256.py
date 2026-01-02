import sys
import time
input = sys.stdin.readline

def find(tree,x):
    idx = tree[x][0]
    if(idx== x):
        return x
    else:
        root_idx = find(tree,idx)
        return root_idx

def unite(tree,x,y,w):
    x_root_idx = find(tree,x)
    y_root_idx = find(tree,y)

    if not (x_root_idx == y_root_idx):
        if(tree_rank[x_root_idx] < tree_rank[y_root_idx]):
            tree[x_root_idx] = (y_root_idx,w)
        else:
            tree[y_root_idx] = (x_root_idx,w)
            if(tree_rank[x_root_idx] == tree_rank[y_root_idx]):
                tree_rank[x_root_idx] = tree_rank[x_root_idx] + 1

def same(tree,x,y):
    x_root_idx = find(tree,x)
    y_root_idx = find(tree,y)
    if(x_root_idx == y_root_idx):
        return True
    else:
        return False

v_num,e_num = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(e_num)]
union_find_tree = [(i,0) for i in range(v_num)]
tree_rank = [0]*v_num
if __name__ == "__main__":
    edges.sort(key=lambda x:x[2])
    for e in edges:
        unite(union_find_tree,e[0],e[1],e[2])
    print(sum(item[1] for item in union_find_tree))



