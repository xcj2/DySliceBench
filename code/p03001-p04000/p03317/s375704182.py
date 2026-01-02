import sys
def input(): return sys.stdin.readline().strip()

def func(n, k):
    """
    n個のものをk個ずつ重なり1でとる回数
    """
    if n <= 1: return 0
    if n <= k: return 1
    if (n - k) % (k - 1) == 0: return 1 + (n - k) // (k - 1)
    return 1 + (n - k) // (k - 1) + 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    place = 0
    for i in range(N):
        if A[i] == 1:
            place = i
            break
    """
    1を常に端点にとると失敗する！
    反例：A=[2,3,4,1,5,6,7], K=3
    """
    ans = 10**10
    for i in range(K):
        ans1 = func(place - i + 1, K)
        ans2 = func((N - place) - (K - i) + 1, K)
        #print("i={}, ans1={}, ans2={}".format(i, ans1, ans2))
        ans = min(ans, ans1 + ans2 + 1)
    print(ans)

if __name__ == "__main__":
    main()
