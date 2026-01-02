par = [i for i in range(100)]
rank = [0 for i in range(100)]
weight_to_root = [0 for i in range(100)]

def find(x):
    if par[x] == x:
        return x
    else:
        root = find(par[x])
        weight_to_root[x] += weight_to_root[par[x]]
        par[x] = root
        return root

def is_same(x,y):
    return find(x) == find(y)

def union(x,y,w):
    a = find(x)
    b = find(y)
    if a==b:
        return False
    if rank[a] > rank[b]:
        par[b] = a
        weight_to_root[b] = -w - weight_to_root[y] + weight_to_root[x]
    elif rank[a] < rank[b]:
        par[a] = b
        weight_to_root[a] = w - weight_to_root[x] + weight_to_root[y]
    else:
        par[b] = a
        weight_to_root[b] = -w - weight_to_root[y] + weight_to_root[x]
        rank[a] += 1
    return True

def diff(x,y):
    return weight_to_root[x] - weight_to_root[y]


def main():
    global rank,par,weight_to_root
    n,q = [int(i) for i in input().split()]
    rank = [0 for i in range(n)]
    par = [i for i in range(n)]
    weight_to_root = [0 for i in range(n)]
    for i in range(q):
        s = [int(j) for j in input().split()]
        if s[0] == 0:
            union(s[1],s[2],s[3])
        else:
            if is_same(s[1],s[2]):
                print(diff(s[1],s[2]))
            else:
                print('?')

if __name__ == '__main__':
    main()
