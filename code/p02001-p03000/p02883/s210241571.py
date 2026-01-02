import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort(reverse=True)  # 0(NlogN)
    F.sort()  # O(NlogN)

    def train(X, Y, T):  # O(N)    ans: 回数
        ans = 0
        for i in range(len(X)):
            ans += max(0, X[i] - T // Y[i])
        return ans

    ok = 10**18+1 #時間
    ng = -1

    while ok - ng > 1:
        mid = (ok + ng) // 2 #時間
        ans = train(A,F,mid)  #kaisuu
        if ans >K:
            ng =mid
        else:
            ok =mid

    print(ok)


if __name__ == "__main__":
    main()
