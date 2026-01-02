from collections import defaultdict

n, m = map(int, input().split())
t = [tuple(map(int, input().split())) for _ in range(m)]

#各ノードの根（-1はそのノードが根）
follow = [-1]*n
#（自分を含む）連結している数
num_follower = [1]*n

def root_index_of(A):
    r = A
    while follow[r] > -1:
        r = follow[r]
    return r

def connected(A,B):
    return root_index_of(A) == root_index_of(B)

now = 0
def connect(A,B):
    global now
    rA = root_index_of(A)
    rB = root_index_of(B)
    if rA == rB:
        return
    now += num_follower[rA]*num_follower[rB]
    if num_follower[rA] < num_follower[rB]:
        follow[rA] = rB
        follow[A] = rB
        num_follower[rB] += num_follower[rA]
    else:
        follow[rB] = rA
        follow[B] = rA
        num_follower[rA] += num_follower[rB]


c = n*(n-1)//2
ans = [c]
for i in range(m-1, 0, -1):
    a, b = t[i]
    connect(a-1, b-1)
    ans.append(c-now)
for i in range(m-1, -1, -1):
    print(ans[i])

