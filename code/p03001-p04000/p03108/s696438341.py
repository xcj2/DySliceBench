N, M = [int(i) for i in input().split()]
data_ls = list()
for i in range(M):
    data_ls.append([int(i) -1 for i in input().split()])
A_ls, B_ls = zip(*data_ls)
conv_ls = list()

par = list(range(N))
rank = [1] * N

def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def unite(x, y):
    x = find(x)
    y = find(y)
    if rank[x] < rank[y]:
        par[x] = y
        rank[y] += rank[x]
        rank[x] = rank[y]
    else:
        par[y] = x
        rank[x] += rank[y]
        rank[y] = rank[x]

def is_same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False

def ranking(x):
    return rank[find(x)]

def main():
    conv_ls.append(0)
    for i, (x,y) in enumerate(data_ls[::-1]):
        N1 = ranking(x)
        N2 = ranking(y)
        if is_same(x, y):
            conv_ls.append(conv_ls[i])
        else:
            conv_ls.append(conv_ls[i] + N1 * N2)
            unite(x,y)
    for conv in conv_ls[::-1][1:]:
        print(int(N * (N - 1) / 2 - conv))

main()