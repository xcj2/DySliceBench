# 再帰呼び出しのとき付ける
import sys
sys.setrecursionlimit(10**9)

def readInt():
    return list(map(int, input().split()))

n, m = readInt()

root = [-1] * n

def r(x):
    # print("root[x]=",root[x])
    if root[x] < 0:
        # print("r(x)=",x)
        return x
    else:
        root[x] = r(root[x])
        # print(root[x])
        return root[x]

def unite(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    root[x] += root[y]
    root[y] = x
    # print(root)

def size(x):
    x = r(x)
    # print(x, root[x])
    return -root[x]

for i in range(m):
    x, y = readInt()
    x -= 1
    y -= 1
    unite(x, y)
    # print('size={}'.format(size(i)))

# max_size = 0

# for i in range(n):
#     max_size = max(max_size, size(i))

# print(max_size)

# print(root)
ans = -1
for i in root:
    if i < 0:
        ans += 1
print(ans)