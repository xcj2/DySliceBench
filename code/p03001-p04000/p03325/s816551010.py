def main():
    """
    1 <= N <= 10^4
    1 <= ai <= 10^9
    """
    N = int(input())
    A = map(int, input().split())

    ans = f(N, A)
    print(ans)


def f(N, A):
    """
    以下の操作をできるだけ多くの回数繰り返す

    1 ≤ i ≤ N を満たす全ての i に対して,
    どちらかを行う.  
        ai の値を 2で割る
        aiの値を 3倍する
    ただし,
        全ての i に対して 3倍することはできず
        操作後の aiの値は整数でなければならない


    2の倍数でなければ2で割れない
    2で割って奇数になった場合、その後は3倍にしかできない
    操作後の数値上限はないので、1つでも2で割れれば良い
    """
    ans = sum(p(a) for a in A)

    return ans


def p(a):
    ans = 0
    while a > 0:
        if a % 2 == 0:
            ans += 1
            a //= 2
        else:
            break
    return ans


if __name__ == '__main__':
    main()
