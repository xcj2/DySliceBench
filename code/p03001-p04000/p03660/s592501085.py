from sys import stdin, setrecursionlimit
def input():
    return stdin.readline().strip()

setrecursionlimit(10**5)

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    edge[i].append(j)
    edge[j].append(i)

# root: 0
# edge1: parent→children
# edge2: child→parent
# tfに探索済かどうかを保存する
tf = [False] * n
tf[0] = True
edge1 = [[] for _ in range(n)]
edge2 = [-1] * n

def divide(i):
    for j in edge[i]:
        if tf[j]:
            continue
        else:
            tf[j] = True
            edge1[i].append(j)
            edge2[j] = i
            divide(j)

divide(0)

now = n - 1
l = [n-1]
while edge2[now] != -1:
    now = edge2[now]
    l.append(now)

root = l[len(l)//2 - 1]

def divide2(i):
    ans = 1
    for j in edge1[i]:
        ans += divide2(j)
    return ans

Snuke = divide2(root)
Fennec = n - Snuke

if Snuke < Fennec:
    print('Fennec')
else:
    print('Snuke')