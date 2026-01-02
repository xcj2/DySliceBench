def main():
    N = int(input())
    C = []
    S = []
    F = []
    for i in range(1, N):
        c, s, f = map(int, input().split())
        C.append(c)
        S.append(s)
        F.append(f)

    AC(N, C, S, F)


def AC(N, C, S, F):
    for i in range(N):
        t = 0
        for j in range(i, N - 1):
            t = t_func(t, C[j], S[j], F[j])

        print(t)


def t_func(t, c, s, f):
    if t < s:
        # 開通式終了前、終了待ってから次の駅(今までのtに依存しない)
        return s + c
    elif t % f == 0:
        # 開通式終了済み、ちょうど列車が発車しているか
        return t + c
    else:
        # 終了済みだが、列車待ち
        return t + (f - t % f) + c
        # t + (f - t  % f)
        # => (t // f + 1) * f
        # => t // f: 余りを気にせず商を求める
        ((t - t % f) // f + 1) * f
        (t - t % f) + f


def WA(N, C, S, F):
    # 逆順に計算して、結果の再利用
    res = [0] * N
    for i in range(1, N):
        res[i] = res[i - 1] + C[-i]
    # 後続の列車より早くない
    for i in range(1, N):
        res[i] = max(res[i - 1], res[i] + S[-i])

    for r in reversed(res):
        print(r)

if __name__ == '__main__':
    main()
