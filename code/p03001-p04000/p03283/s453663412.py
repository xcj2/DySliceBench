def cin():  return list(map(int,input().split()))

N, M, Q = list(map(int,input().split()))
v = [[0 for _ in range(N)] for _ in range(N)]
p = [[0 for _ in range(2)] for _ in range(Q)]

for _ in range(M):
    a, b = cin()
    v[a - 1][b - 1] += 1;

for i in range(Q):
    a, b = cin()
    p[i][0] = a - 1;
    p[i][1] = b - 1;
    
def d2_add(a):
    w = len(a[0])
    h = len(a)
    da = [[0] * w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1, w):
        da[0][i] = da[0][i - 1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i - 1][j] + cnt_w
    return da

def d2_calc(da, x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:  return 0
    if x1 == 0 and y1 == 0:  return da[x2][y2]
    if x1 == 0:  return da[x2][y2] - da[x2][y1 - 1]
    if y1 == 0:  return da[x2][y2] - da[x1 - 1][y2]
    return da[x2][y2] - da[x1 - 1][y2] - da[x2][y1 - 1] + da[x1 - 1][y1 - 1]

ret = d2_add(v)
for i in range(Q):
    ans = d2_calc(ret, p[i][0], p[i][0], p[i][1], p[i][1])
    print(ans)