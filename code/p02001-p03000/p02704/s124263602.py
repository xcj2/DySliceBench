from functools import reduce


def add_row(ans, n, i, k):
    for j in range(n):
        ans[i][j] |= k


def add_column(ans, n, j, k):
    for i in range(n):
        ans[i][j] |= k


def solve(n, sss, ttt, uuu, vvv):
    max_d = max(max(uuu).bit_length(), max(vvv).bit_length())
    ans = [[0] * n for _ in range(n)]

    for d in range(max_d):
        k = 1 << d
        ambiguous_i = []
        ambiguous_j = []
        filled_i = [False, False]
        filled_j = [False, False]
        for i, (s, u) in enumerate(zip(sss, uuu)):
            if s == 0:
                if u & k:
                    add_row(ans, n, i, k)
                    filled_i[1] = True
                else:
                    ambiguous_i.append((i, 0))
            else:
                if u & k:
                    ambiguous_i.append((i, 1))
                else:
                    filled_i[0] = True
        for j, (t, v) in enumerate(zip(ttt, vvv)):
            if t == 0:
                if v & k:
                    if filled_i[0]:
                        return -1
                    add_column(ans, n, j, k)
                    filled_j[1] = True
                else:
                    ambiguous_j.append((j, 0))
            else:
                if v & k:
                    ambiguous_j.append((j, 1))
                else:
                    if filled_i[1]:
                        return -1
                    filled_j[0] = True

        # print(d)
        # print(ans)
        # print(ambiguous_i)
        # print(ambiguous_j)

        # print(*map('{:064b}'.format, [k] * (n + 1)))
        # for i in range(n):
        #     print(*map('{:064b}'.format, ans[i]), end=' ')
        #     print('{:064b}'.format(uuu[i]))
        # print(*map('{:064b}'.format, vvv))
        # print(ambiguous_i, ambiguous_j)
        # print(filled_i, filled_j)
        # print()

        if len(ambiguous_i) == 0:
            amb = set(bj for j, bj in ambiguous_j)
            for bj in amb:
                if not filled_i[bj]:
                    return -1
        elif len(ambiguous_j) == 0:
            amb = set(bi for i, bi in ambiguous_i)
            for bi in amb:
                if not filled_j[bi]:
                    return -1
        elif len(ambiguous_i) == 1:
            i, bi = ambiguous_i[0]
            if filled_j[bi]:
                for j, bj in ambiguous_j:
                    if bj:
                        ans[i][j] |= k
            elif filled_i[bi ^ 1]:
                if bi:
                    for j, bj in ambiguous_j:
                        ans[i][j] |= k
            else:
                ok = False
                for j, bj in ambiguous_j:
                    if bj:
                        ans[i][j] |= k
                    if bi == bj:
                        ok = True
                if not ok:
                    return -1
        elif len(ambiguous_j) == 1:
            j, bj = ambiguous_j[0]
            if filled_i[bj]:
                for i, bi in ambiguous_i:
                    if bi:
                        ans[i][j] |= k
            elif filled_j[bj ^ 1]:
                if bj == 1:
                    for i, bi in ambiguous_i:
                        ans[i][j] |= k
            else:
                ok = False
                for i, bi in ambiguous_i:
                    if bi:
                        ans[i][j] |= k
                    if bi == bj:
                        ok = True
                if not ok:
                    return -1
        else:
            for ii, (i, bi) in enumerate(ambiguous_i):
                for jj, (j, bj) in enumerate(ambiguous_j):
                    if (ii ^ jj) & 1:
                        ans[i][j] |= k

    return ans


def debug(n, sss, ttt, uuu, vvv, ans):
    from operator import or_, and_
    dbg = [row.copy() for row in ans]
    for i in range(n):
        func = and_ if sss[i] == 0 else or_
        dbg[i].append(reduce(func, dbg[i]))
        dbg[i].append(uuu[i])
    vertical = []
    correct = []
    for j in range(n):
        func = and_ if ttt[j] == 0 else or_
        vertical.append(reduce(func, (dbg[i][j] for i in range(n))))
        correct.append(vvv[j])
    dbg.append(vertical)
    dbg.append(correct)

    for row in dbg:
        print(*map('{:064b}'.format, row))


n = int(input())
sss = list(map(int, input().split()))
ttt = list(map(int, input().split()))
uuu = list(map(int, input().split()))
vvv = list(map(int, input().split()))

ans = solve(n, sss, ttt, uuu, vvv)
if ans == -1:
    print(ans)
else:
    for row in ans:
        print(*row)
