# coding: utf-8

# https://atcoder.jp/contests/abc119


def leq_search(xs, x, s, t):
    # x以下で最大のindex
    if t-s <= 3:
        res = 0
        for i in range(s, t):
            if xs[i] <= x:
                res = i
        return res

    i = (s+t)//2
    if xs[i] <= x:
        return leq_search(xs, x, i, t)
    else:
        return leq_search(xs, x, s, i)


def geq_search(xs, x, s, t):
    # x以上で最小のindex
    if t-s <= 3:
        res = 0
        for i in range(t-1, s-1, -1):
            if xs[i] >= x:
                res = i
        return res

    i = (s+t)//2
    if xs[i] >= x:
        return geq_search(xs, x, s, i+1)
    else:
        return geq_search(xs, x, i+1, t)


def nearest_search(xs, x, s, t):
    # xにもっとも近いindex
    if t-s <= 3:
        res = s
        for i in range(s, t):
            if abs(x-xs[i]) < abs(x-xs[res]):
                res = i
        return res

    i = (s+t)//2
    if xs[i] <= x:
        return nearest_search(xs, x, i, t)
    else:
        return nearest_search(xs, x, s, i+1)


def main():
    A, B, Q = map(int, input().split())
    s = [None] * A
    t = [None] * B
    xs = [None] * Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        xs[i] = int(input())

    S, T = 0, 1
    st = [[s[i], S, i] for i in range(A)]
    st.extend([[t[i], T, i] for i in range(B)])
    # st = [[s[i], S, i] for i in range(A)].extend([[t[i], T, i] for i in range(B)])
    st = sorted(st, key=lambda x: x[0])
    st_retrieval = [x[0] for x in st]

    # 各神社から最寄りの寺を求める
    s_near_t = [None] * A
    for i in range(A):
        s_near_t[i] = t[nearest_search(t, s[i], 0, B)]

    # 各寺から最寄りの神社を求める
    t_near_s = [None] * B
    for i in range(B):
        t_near_s[i] = s[nearest_search(s, t[i], 0, A)]

    for x in xs:
        # left
        near_i = leq_search(st_retrieval, x, 0, A+B)
        val, mark, i = st[near_i]
        # val: 座標
        # mark: S or T
        # i: 元の列 s or t の中での index
        cand1 = abs(val-x)
        if mark == S:
            near_t = s_near_t[i]
            cand1 += abs(near_t-val)
        else:
            near_s = t_near_s[i]
            cand1 += abs(near_s-val)

        # right
        near_i = geq_search(st_retrieval, x, 0, A+B)
        val, mark, i = st[near_i]
        # val: 座標
        # mark: S or T
        # i: 元の列 s or t の中での index
        cand2 = abs(val-x)
        if mark == S:
            near_t = s_near_t[i]
            cand2 += abs(near_t-val)
        else:
            near_s = t_near_s[i]
            cand2 += abs(near_s-val)
        
        print(min(cand1, cand2))


main()
# print(main())
