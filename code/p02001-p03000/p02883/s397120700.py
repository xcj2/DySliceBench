import sys


# \n
def input():
    return sys.stdin.readline().rstrip()

def train(X, Y, T):  # O(N)    ans: 回数
    ans = 0
    for i in range(len(X)):
        ans += max(0, X[i] - T // Y[i])
    return ans


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort(reverse=True)  # 0(NlogN)
    F.sort()  # O(NlogN)

    t =A[0]*(10**6)

    if K>=t:
        print(0)
        exit()

    ok = t+1 #時間
    ng = -1

    # O(Nlog(maxK)?)
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
