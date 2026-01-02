import sys

sys.setrecursionlimit(10 ** 5 + 5)


# 2乗の木DP

def prepare(n, MOD):
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


def nhr(factorials, invs, n, r, MOD):
    return factorials[n + r - 1] * invs[n - 1] * invs[r] % MOD


def dfs0(links):
    q = [(0, -1)]
    while q:
        v, p = q.pop()
        links[v].discard(p)
        links[v] = list(links[v])
        q.extend((u, v) for u in links[v])


def dfs1(links, st_count_fwd, st_count_bwd, st_pattern_fwd, st_pattern_bwd):
    q = [(0, -1, 0)]
    while q:
        v, p, o = q.pop()
        if o == 0:
            # 初回訪問
            q.append((v, p, 1))
            q.extend((u, v, 0) for u in links[v])
        else:
            # 子の探索が終わった後の砲門
            curr_count = [0]
            curr_pattern = [1]
            for u in links[v]:
                stc_u = st_count_fwd[u][-1] + 1
                new_pattern = factorials[curr_count[-1] + stc_u] * invs[curr_count[-1]] * invs[stc_u] % MOD
                curr_pattern.append(new_pattern * curr_pattern[-1] * st_pattern_fwd[u][-1] % MOD)
                curr_count.append(curr_count[-1] + stc_u)
            st_count_fwd[v] = curr_count
            st_pattern_fwd[v] = curr_pattern
            curr_count = [0]
            curr_pattern = [1]
            for u in reversed(links[v]):
                stc_u = st_count_fwd[u][-1] + 1
                new_pattern = factorials[curr_count[-1] + stc_u] * invs[curr_count[-1]] * invs[stc_u] % MOD
                curr_pattern.append(new_pattern * curr_pattern[-1] * st_pattern_fwd[u][-1] % MOD)
                curr_count.append(curr_count[-1] + stc_u)
            st_count_bwd[v] = curr_count[::-1]
            st_pattern_bwd[v] = curr_pattern[::-1]


def dfs2(links, st_count_fwd, st_count_bwd, st_pattern_fwd, st_pattern_bwd, ans):
    def sub(v, pc, pp):
        # print(v, pc, pp)
        if pc == 0:
            ans[v] = st_pattern_fwd[v][-1]
        else:
            cc = st_count_fwd[v][-1]
            cp = st_pattern_fwd[v][-1]
            pattern = factorials[cc + pc] * invs[cc] * invs[pc] % MOD
            pattern = pattern * cp * pp % MOD
            ans[v] = pattern

        for i, u in enumerate(links[v]):
            fc = st_count_fwd[v][i]
            fp = st_pattern_fwd[v][i]
            bc = st_count_bwd[v][i + 1]
            bp = st_pattern_bwd[v][i + 1]
            p1 = factorials[fc + bc] * invs[fc] * invs[bc] % MOD
            p1 = p1 * fp * bp % MOD
            p2 = factorials[fc + bc + pc] * invs[fc + bc] * invs[pc] % MOD
            p2 = p2 * p1 * pp % MOD
            # print(v, u, fc, fp, bc, bp, p1, p2)
            sub(u, fc + bc + pc + 1, p2)

    sub(0, 0, 1)


n, *ab = map(int, sys.stdin.buffer.read().split())
links = [set() for _ in range(n)]
for a, b in zip(ab[0::2], ab[1::2]):
    a -= 1
    b -= 1
    links[a].add(b)
    links[b].add(a)
MOD = 10 ** 9 + 7
factorials, invs = prepare(n, MOD)
st_count_fwd = [[] for _ in range(n)]
st_count_bwd = [[] for _ in range(n)]
st_pattern_fwd = [[] for _ in range(n)]
st_pattern_bwd = [[] for _ in range(n)]
ans = [0] * n

dfs0(links)
dfs1(links, st_count_fwd, st_count_bwd, st_pattern_fwd, st_pattern_bwd)
# print(st_count_fwd, st_count_bwd, st_pattern_fwd, st_pattern_bwd, sep='\n')
dfs2(links, st_count_fwd, st_count_bwd, st_pattern_fwd, st_pattern_bwd, ans)
print('\n'.join(map(str, ans)))
