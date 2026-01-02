def main():
    """
    1 <=  D <= 100
    1 <= pi <= 100
    1 <=  i <= D
    100 <= G
    100 <= ci <= 10^6

    all: sum(p)
        max: 100 * 10 = 1000
    """
    D, G = map(int, input().split())
    P, C = zip(*(
        map(int, input().split())
        for _ in range(D)
    ))

    # ans = f(D, G, P, C)
    ans = editorial(D, G, P, C)
    print(ans)


def editorial(D, G, P, C):
    ans = float("inf")
    for i in range(2 ** D):
        c = 0
        score = 0
        clear = [False] * D
        for j in range(D):
            if i & (1 << j):
                c += P[j]
                score += 100 * (j + 1) * P[j] + C[j]
                clear[j] = True

        # print(i, clear, c, score)
        for j in range(D)[::-1]:
            if score >= G:
                break
            if clear[j]:
                continue

            rest = G - score
            base_score = 100 * (j + 1)
            add_c = (rest + base_score - 1) // base_score
            add_c = min(add_c, P[j] - 1)
            c += add_c
            score += base_score * add_c

            # print("\t", base_score, c, score)

        if score >= G:
            ans = min(ans, c)

    return ans


def f(D, G, P, C):
    """
    i, P から問題をすべて分割
    すべての解き方を列挙する
    sum_p ! = 1000 ! => TLE

    点数の高いものから解けばいいとは限らない

    dpっぽく前の解き方を利用してみる
    ans[0] = 0
    ans[1] = max_i * 100 or ボーナスあり
        ボーナスがあるので、前の答え＋点の良い問題とは限らない
        前の解き方のうち、１つ変えるとどうなるか？
            ボーナスがなくなってしまうかもしれない
            代わりにボーナスになる可能性もある
            前の解き方からｘ問変えるとどうなるか？
                同様
    ボーナスもらえるテーブルを作る？
        それとボーナス加味しないDPテーブルとの比較
        b_dp[5] = p1 全完了
        dp[2] = p2
            fix[]
    """
    from itertools import permutations
    from collections import defaultdict

    sum_p = sum(P)
    dp = [float("inf") for _ in range(sum_p + 1)]
    dp[0] = 0
    max_state = {}

    # 総スコアと効率、
    total = [(i + 1) * 100 * P[i] + C[i] for i in range(D)]
    ratio = [total[i] / P[i] for i in range(D)]
    bonus = [False for _ in range(D)]
    for i in range(1, sum_p + 1):
        score = 0
        rest = i
        for j in range(D):
            if bonus[j]:
                rest -= P[j]
                score += total[j]
            elif P[j] <= rest:
                bonus[j] = True
                rest -= P[j]
                score += total[j]

        if dp[i] >= G:
            return i


if __name__ == '__main__':
    main()
