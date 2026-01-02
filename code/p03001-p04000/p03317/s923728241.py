import sys
import math
     
     
def main():
    """
    2 <= K <= N <= 10^5
    1 <= ai <= N
    1 <= i <= N
    """
    N, K = map(int, input().split())
    *A, = map(int, input().split())
 
    #ans = f_K(N, K, A)
    ans = editorial(N, K, A)
    print(ans)
     
     
def test_examples():
    nka_ans = [
        (4, 3, [2, 3, 1, 4], 2),
        (3, 3, [1, 2, 3], 1),
        (8, 3, [7, 3, 1, 8, 4, 6, 2, 5], 4),
    ]
 
    for N, K, A, ans in nka_ans:
        assert editorial(N, K, A) == ans
        assert f_K(N, K, A) == ans
     
     
def test_ans():
    nka_ans = [
        (5, 2, [1, 2, 3, 4, 5], 4),
        (5, 3, [1, 2, 3, 4, 5], 2),
        (5, 2, [5, 4, 3, 2, 1], 4),
        (5, 3, [5, 4, 3, 2, 1], 2),
    ]
     
    for N, K, A, ans in nka_ans:
        assert editorial(N, K, A) == ans
        assert f_K(N, K, A) == ans
     
     
def f_K(N, K, A):
    """
    最初に置く範囲は、 1_idx - K + 1 から 1_idx
    """
    idx = [i for i, a in enumerate(A) if a == 1][0]
    left_idx = max(0, idx - K)
    ans = float("inf")
    for i in range(left_idx, idx + 1):
        left = i
        right = max(0, N - left - K)
        tmp = (left + (K - 1) - 1) // (K - 1)
        tmp += 1
        tmp += (right + (K - 1) - 1) // (K - 1)
        ans = min(ans, tmp)
     
    return ans
     
     
def editorial(N, K, A):
    """
    端から端までカバーしていく
    K + (K - 1) * N (N >= 0)
    これは仮に１番左に1があったとき
    結果的には順番は気にしなくて良い
    上記でカバーしていくと、いつかは最初の1をカバーする
        カバーした順番を1をカバーしたことを最初に行えば変わらない
     
    TODO: editorial pdfの意味
        1 + g(K − 1) ≤ p ≤ 1 + (g + 1)(K − 1) なる整数 g
    """
    return ((N-1) + (K-1) - 1) // (K-1)
     
     
     
if __name__ == '__main__':
    main()