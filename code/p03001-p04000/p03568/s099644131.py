from itertools import product


def main():
    N = int(input())
    A = map(int, input().split())

    f(N, A)


def f2(N, A):
    """
    Bの項どれか1つは偶数
    B = A, A+1, A-1
    Aの項が奇数: Bは奇数1,偶数2
    Aの項が偶数: Bは奇数2,偶数1
    B1が偶数なら、B2以降は似ていればなんでも良い
    B1が奇数なら、B2以降のどれかは似ていいるかつ偶数

    全列挙しなくてもAの項の偶奇性を使ってO(N)で計算できそう
    """
    pass


def f(N, A):
    """全組み合わせ

    3^10=59,049
    """
    B = [
        (a, a+1, a-1)
        for a in A
    ]
    ans = 0
    for b in product(*B):
        p = 1
        for _b in b:
            p *= _b
        if p % 2 == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
