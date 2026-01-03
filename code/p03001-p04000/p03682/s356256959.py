n = int(input())
z = []
for i in range(n):
    X, Y = map(int, input().split())
    z.append([X, Y, i])

x = sorted(z, key=lambda x: x[0])
y = sorted(z, key=lambda x: x[1])

new_list = []
for i in range(n-1):
    new_list.append([x[i+1][0]-x[i][0], x[i+1][2], x[i][2]])
    new_list.append([y[i+1][1]-y[i][1], y[i+1][2], y[i][2]])

new_list.sort(key=lambda x: x[0])

# Union-Find  ---------------
parent = [i for i in range(n)]
rank = [0 for i in range(n)]

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

from collections import deque
q = deque(new_list)

cost = 0
while len(q)>0:
    c = q.popleft()
    if not judge(c[1], c[2]):
        merge(c[1], c[2])
        cost += c[0]

print(cost)