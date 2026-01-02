def resolve():
    import sys

    def LI():
        return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり

    def S():
        return sys.stdin.readline().rstrip()

    N, M = map(int, S().split())
    A = LI()
    A.sort()

    def f(n,x):  # A[n]+A[i]>=x となる i の最小値
        left = -1
        right = N
        while left + 1 < right:
            mid = (left + right) // 2
            if A[n] + A[mid] < x:
                left = mid
            else:
                right = mid
        return right

    low = 2 * A[0]
    high = 2 * A[-1] + 1

    while low + 1 < high:
        mid = (low + high) // 2
        if sum(N - f(i,mid) for i in range(N)) >= M:
            low = mid
        else:
            high = mid

    a = low  # a以上のA[i]+A[j]がM個以上となる最大のa

    from itertools import accumulate

    B = [0] + list(accumulate(A))

    r = 0
    ans = 0
    for i in range(N):  # a+1以上のA[i]+A[j]を足し合わせていく
        b = f(i,a+1)
        r += N - b
        ans += B[N] - B[b]
        ans += A[i] * (N - b)

    ans += (M - r) * a  # A[i]+A[j] == a となるものを足し合わせる

    print(ans)

if __name__ == '__main__':
    resolve()