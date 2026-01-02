
def init(N, parent, rank):
    for i in range(N):
        parent.append(i)
        rank.append(0)
    return parent, rank

def find(parent, v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent, parent[v])
        return parent[v]

def unite(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return 
    elif rank[a] < rank[b]:
        parent[a] = b
        return parent
    elif rank[a] > b:
        parent[b] = a
        return parent
    else:
        parent[b] = a
        rank[a] += 1
        return parent, rank

def union_find():
    N, Q = [int(i) for i in input().split()]
    parent = []
    rank = []
    init(N, parent, rank)
    for i in range(Q):
        P, A, B = [int(i) for i in input().split()]
        if P == 0:
            unite(parent, rank, A, B)
        else:
            a = find(parent, A)
            b = find(parent, B)
            if a == b:
                print("1")
            else:
                print("0")

if __name__ == "__main__":
    union_find()

