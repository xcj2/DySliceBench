from collections import Counter
from bisect import bisect_left


def main():
    N, M = map(int, input().split())
    *A, = map(int, input().split())
    BC = [
        list(map(int, input().split()))
        for _ in range(M)
    ]

    ans = f_replace(N, M, A, BC)
    ans1 = ref(N, M, A, BC)
    assert ans == ans1
    print(ans)


def ref(N, M, A, BC):
    """
    元々のAをBCと混ぜて最大化するようにN個選ぶ
    全体は2 * (10^5) なので、sortを考慮しても問題ない
    """
    counter = Counter(A)
    for b, c in BC:
        counter[c] += b

    ans = 0
    rem = N
    vn = sorted(counter.items(), key=lambda x: -x[0])
    for v, n in vn:
        use = min(n, rem)
        ans += use * v
        rem -= use

    return ans


def f_replace(N, M, A, BC):
    """
    2分探索なんて必要なかった
    順々に変更する要素を見つけ、変える必要がなければ終了
    """
    A = sorted(A)
    BC = sorted(BC, key=lambda x: -x[1])
    i = 0
    for b, c in BC:
        if i >= N:
            break
        for _ in range(b):
            if i >= N:
                break
            elif A[i] < c:
                A[i] = c
                i += 1
            else:
                i = N
                break

    ans = sum(A)
    return ans


def WA_RE(N, M, A, BC):
    """
    A,Cの値: 10^9
        配列用意できない
    A,BCの数: 10^5

    書き換えると順番がバラバラになる
    個数10^5より、実際の種類数は10^5
    2分探索？

    BCに着目
    最大にする書き換え方を検証する
    """

    A = sorted(A)
    min_a = A[0]
    min_pos = 0

    # 小さい値から、大きい値に書き換える
    bc = sorted(BC, key=lambda x: -x[1])
    bc = list(filter(lambda x: x[1] > min_a, bc))
    ans = 0
    for b, c in bc:
        # 入れ替える必要の確認
        # cはだんだん小さくなり、min_aは大きくなるため
        if c < min_a:
            break
        # 二分探索を行えるように最小値の設定
        pos = bisect_left(A, c, lo=min_a)
        # if pos >= N:
        #    break

        # 書き換えすぎないように設定
        pos_to = min(min_pos + b, pos)
        for i in range(min_pos, pos_to):
            # 比較対象はだんだんと右にずれるので、計算量はAの数だけ
            # bだけ書き換えるが、大きい場合は対象外
            if A[i] < c:
                ans += c
            else:
                break

        min_pos = i + 1
        min_a = A[i]

    ans += sum(A[min_pos:])
    return ans


def TLE(N, M, A, BC):
    for b, c in BC:
        A = sorted(A)
        for i in range(b):
            if A[i] < c:
                A[i] = c
            else:
                break

    ans = sum(A)
    return ans


def editorial(N, M, A, BC):
    ans = 0
    return ans


if __name__ == '__main__':
    main()
