from collections import Counter


def main():
    r"""
    数列 a1,a2,...,anが以下の条件を満たすとき、 /\/\/\/ と呼ぶ

        各 i=1,2...,n-2 について、ai=ai+2
        数列に現れる数はちょうど 2種類偶数長の数列

    v1,v2,...,vnが与えられます
    要素をいくつか書き換えることでこの数列を /\/\/\/ にしたいです。
    書き換える要素の数は最小でいくつになるか求めてください。

    2 <= n <= 10^5, nは偶数
    1 <= vi <= 10^5, viは整数
    """
    n = int(input())
    *v, = map(int, input().split())

    ans = f(n, v)
    assert ans == simple(n, v)
    print(ans)


def simple(n, v):
    # most_commonを事前に使い短くする
    # 1種類しかないならば存在しない種類を0個で足して条件分岐を潰す
    c1 = Counter(v[::2]).most_common() + [(0, 0)]
    c2 = Counter(v[1::2]).most_common() + [(0, 0)]

    if c1[0][0] == c2[0][0]:
        n_no_change = max(c1[0][1] + c2[1][1],
                          c1[1][1] + c2[0][1])
        return n - n_no_change
    else:
        return n - c1[0][1] - c2[0][1]

def f(n, v):
    """
    3 1 3 2:
        3種類
        a1=a3, a2 != a4
    """
    ans = float("inf")
    v_idx_even = []
    v_idx_odd = []
    for i, x in enumerate(v):
        if i % 2 == 0:
            v_idx_even.append(x)
        else:
            v_idx_odd.append(x)

    ve = Counter(v_idx_even)
    vo = Counter(v_idx_odd)

    if len(ve) == 1 and len(vo) == 1:
        # 両方1種類
        ans = 0
        if ve.most_common()[0][0] == vo.most_common()[0][0]:
            ans = n // 2

    elif len(ve) == 1 or len(vo) == 1:
        # 片方1種類
        idx = 0
        if ve.most_common()[0][0] == vo.most_common()[0][0]:
            idx = 1
        if len(ve) == 1:
            ans = n // 2 - vo.most_common()[idx][1]
        else:
            ans = n // 2 - ve.most_common()[idx][1]

    else:
        # 両方2種類以上
        if ve.most_common()[0][0] != vo.most_common()[0][0]:
            ans = n - ve.most_common()[0][1] - vo.most_common()[0][1]
        else:
            ans = n - \
                max(ve.most_common()[0][1] + vo.most_common()[1][1],
                    ve.most_common()[1][1] + vo.most_common()[0][1])

    return ans


if __name__ == '__main__':
    main()
