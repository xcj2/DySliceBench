n, q = map(int, input().split(" "))
parent = [i for i in range(n)]
rank = [0] * len(parent)

def root(s):
    if parent[s] == s:
        return s
    else:
        parent[s] = root(parent[s])
        return parent[s]

def same(s1, s2):
    if root(s1) == root(s2):
        print("1")
    else:
        print("0")

def unite(s1, s2):
    s1 = root(s1)
    s2 = root(s2)

    if s1 == s2:
        return

    if rank[s1] < rank[s2]:
        parent[s1] = s2
    else:
        parent[s2] = s1
        if rank[s1] == rank[s2]:
            rank[s1] += 1

for i in range(q):
    query, item1, item2 = input().split(" ")
    item1, item2 = int(item1), int(item2)

    if query == "0":
        unite(item1, item2)
    else:
        same(item1, item2)