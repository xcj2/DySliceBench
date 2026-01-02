# ノイローゼなりかけたので答え見た
# unionfind使うのはわかったけど与えられた配列とどうやって合わせて実装するかわからずさらにノイローゼに


n, m = map(int, input().split())

arr = list(map(lambda x: int(x) - 1, input().split()))
par = [i for i in range(n)]


def root(i):
    if i == par[i]:
        return i
    else:
        _i = root(par[i])
        par[i] = _i
        return _i


def union(x, y):
    x, y = root(x), root(y)
    if x != y:
        # yの親をxにする
        par[y] = x


def same(nx, ny):
    return root(nx) == root(ny)


for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    union(x, y)

ans = 0
for i in range(n):
    if same(i, arr[i]):
        ans += 1
print(ans)
