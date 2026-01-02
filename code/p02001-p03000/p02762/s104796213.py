n, m, k = map(int, input().split())
par = [-1 for _ in range(n)]

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])  # 経路圧縮
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    # サイズの大きい木にサイズの小さい木をくっつける。親の直下に親をくっつける。
    # 親のサイズは負の値になっているので、符号に注意
    if par[x] < par[y]:
        par[x] += par[y]
        par[y] = x
    else:
        par[y] += par[x]
        par[x] = y
    return True

friends_num = [0] * 100005
for _ in range(m):
    num_from, num_to = map(int, input().split())
    num_from -= 1
    num_to -= 1
    friends_num[num_from] += 1
    friends_num[num_to] += 1
    unite(num_from, num_to)

blocks = [[] * n for i in range(n)]
for _ in range(k):
    num_from, num_to = map(int, input().split())
    num_from -= 1
    num_to -= 1
    blocks[num_from].append(num_to)
    blocks[num_to].append(num_from)

ans_list = []
for i in range(n):
    ans = -par[find(i)] - friends_num[i] - 1
    for b in blocks[i]:
        if same(i, b):
            ans -= 1
    ans_list.append(ans)

print(' '.join(map(str, ans_list)))