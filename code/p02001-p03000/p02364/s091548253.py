v, e = map(int, input().split())
data = []
for i in range(e):
    data.append(list(map(int, input().split())))

from collections import deque

q = deque(sorted(data, key=lambda x: x[2]))


parent = [i for i in range(v)]
rank = [0 for i in range(v)]

# Union-Find  ---------------
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def judge(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return True
    else:
        return False

def merge(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return
    else:
        if rank[a_parent] > rank[b_parent]:
            parent[b_parent] = a_parent
        elif rank[a_parent] < rank[b_parent]:
            parent[a_parent] = b_parent
        else:
            parent[a_parent] = b_parent
            rank[b_parent] += 1

#----------------------------


ans = 0
while len(q) > 0:
    a = q.popleft()
    if not judge(a[0], a[1]):
        merge(a[0], a[1])
        ans += a[2]

print(ans)
