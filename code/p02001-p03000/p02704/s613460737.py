# F - I hate Matrix Construction

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
u = list(map(int, input().split()))
v = list(map(int, input().split()))
assert len(s) == len(t) == n
assert len(u) == len(v) == n

nbits = 64
AND = 0
OR  = 1

# 初期配列
A = [[u[i]] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if t[j] == AND:
            A[i][j] |= v[j]  # v[j]で1のビットは1
        else:
            A[i][j] &= v[j]  # v[j]で0のビットは0
        # conflict check
        if (s[i] == AND and t[j] == OR  and  u[i] & ~v[j]) or \
           (s[i] == OR  and t[j] == AND and ~u[i] &  v[j]):
            print(-1)
            exit()

def must_set(s, u, ucount, i, k):
    return s[i] == OR  and u[i] & (1 << k) and ucount[i] == 0
def must_clear(s, u, ucount, i, k):
    return s[i] == AND and u[i] & (1 << k) == 0 and ucount[i] == n

def set_pos(t, v, vcount, k):
    "第kビットを1にしてもよい列"
    for j in range(n):
        if t[j] == AND and v[j] & (1 << k) == 0 and vcount[j] < n - 1:
            return j
    raise Exception
def clear_pos(t, v, vcount, k):
    "第kビットを0にしてもよい列"
    for j in range(n):
        if t[j] == OR  and v[j] & (1 << k) and vcount[j] > 1:
            return j
    raise Exception

def check_spec(s, t, u, v, ucount, vcount, i, k, trans):
    if must_set(s, u, ucount, i, k):
        j = set_pos(t, v, vcount, k)
        ucount[i] += 1
        vcount[j] += 1
        if trans: i, j = j, i
        A[i][j] |= 1 << k
    elif must_clear(s, u, ucount, i, k):
        j = clear_pos(t, v, vcount, k)
        ucount[i] -= 1
        vcount[j] -= 1
        if trans: i, j = j, i
        A[i][j] &= ~(1 << k)

# ビットごとの処理
for k in range(nbits):
    # 1の個数
    ucount = [0] * n
    vcount = [0] * n
    for i in range(n):
        for j in range(n):
            if A[i][j] & (1 << k):
                ucount[i] += 1
                vcount[j] += 1

    # 仕様通りでない箇所を修正
    try:
        for i in range(n):
            check_spec(s, t, u, v, ucount, vcount, i, k, False)
        for j in range(n):
            check_spec(t, s, v, u, vcount, ucount, j, k, True)
    except:
        print(-1)
        exit()

for i in range(n):
    print(' '.join(map(str, A[i])))
