import sys
from collections import deque
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


N, M = na()
if N == 1:
    print(1)
    exit()
edge_dic = make_tree_0index(N)


parent_array = [-2] * N
parent_array[0] = -1
node1 = deque([0])
node2 = deque([0])
node3 = deque([0])

while(len(node1)):
    n = node1.popleft()
    for v in edge_dic[n]:
        if parent_array[v] == -2:
            parent_array[v] = n
            node1.append(v)
            node2.append(v)
            node3.append(v)

ans1 = [0] * N

while(len(node2)):
    n = node2.pop()
    ans1[n] = 1
    for v in edge_dic[n]:
        if parent_array[n] == v:
            continue
        ans1[n] = (ans1[n] * (ans1[v]+1)) % M

ans2 = [0] * N

subans2 = [0] * N

while(len(node3)):
    n = node3.popleft()
    ans2[n] = 1
    if n != 0:
        ans2[n] = (ans2[n] * ans2[parent_array[n]] * subans2[n] + 1) % M

    reverse = [1]
    right = 1
    for v in edge_dic[n][::-1]:
        if parent_array[n] == v:
            continue
        right = (right * (ans1[v] + 1)) % M
        reverse.append(right)
    reverse.pop()

    left = 1
    for v in edge_dic[n]:
        if parent_array[n] == v:
            continue
        right = reverse.pop()
        subans2[v] = (left * right) % M
        left = (left * (ans1[v]+1)) % M


ans = [a*b % M for a, b in zip(ans1, ans2)]
print("\n".join(map(str, ans)))
