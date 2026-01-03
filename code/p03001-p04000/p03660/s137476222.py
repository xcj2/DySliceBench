import sys
from collections import deque
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces

def make_tree_0index(N):
    edge_dic = {}
    for _ in range(N-1):
        x, y = na()
        x -= 1
        y -= 1
        if x in edge_dic:
            edge_dic[x].append(y)
        else:
            edge_dic[x] = [y]
        if y in edge_dic:
            edge_dic[y].append(x)
        else:
            edge_dic[y] = [x]
    return edge_dic


N = ni()

edge_dic = make_tree_0index(N)

parent_array = [-2] * N
depth_array = [-1] * N

node = deque([0])
parent_array[0] = -1
depth_array[0] = 0

while(len(node)):
    n = node.popleft()
    for nn in edge_dic[n]:
        if nn == parent_array[n]:
            continue
        parent_array[nn] = n
        depth_array[nn] = depth_array[n] + 1
        node.append(nn)

# print(parent_array,depth_array)

now_depth = depth_array[-1]
max_node = N - 1
for i in range((now_depth-1)//2):
    max_node = parent_array[max_node]

cnt = 1
node.append(max_node)
while(len(node)):
    n = node.popleft()
    for nn in edge_dic[n]:
        if nn == parent_array[n]:
            continue
        node.append(nn)
        cnt += 1

# print(cnt)

if cnt * 2 >= N:
    print("Snuke")
else:
    print("Fennec")