#union-find-tree
def init(n):
    lis = []
    for i in range(n+1):
        lis.append(i)
    return lis
def find(lis, x):
    if lis[x] == x:
        return x
    else:
        lis[x] = find(lis, lis[x])
        return lis[x]
def sameset(lis, x, y):
    return find(lis, x) == find(lis, y)
def union(lis, x, y):
    x = find(lis, x)
    y = find(lis, y)
    if x != y:
        lis[x] = y

N, M = map(int, input().split())
input_lis = [0]+[int(p) for p in input().split()]
union_find_lis = init(N)
for _ in range(M):
    x, y = map(int, input().split())
    union(union_find_lis, x, y)
count = 0
init_flag = True
for index, num in enumerate(input_lis):
    if init_flag:
        init_flag = False
    else:
        if sameset(union_find_lis, index, num):
            count += 1
print(count)