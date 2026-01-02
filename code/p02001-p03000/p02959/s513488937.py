import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N = II()
    A = LI()
    B = LI()

    A_sum = sum(A)  # モンスターの合計数

    # 貪欲

    for i in range(N):
        # まずは自分と同じ番号の町を見る。
        if A[i] >= B[i]: # 街にいるモンスターのほうが多いとき
            A[i] -= B[i]  # 倒せるだけ倒す。
            B[i] = 0
        else: # 勇者の能力のほうが高いとき
            B[i] -= A[i]
            A[i] = 0

        # 次に次の街の面倒を見る。
        if A[i+1] >= B[i]:
            A[i+1] -= B[i]  # 倒せるだけ倒す。
            B[i] = 0
        else: # 勇者の能力のほうが高いとき
            B[i] -= A[i+1]
            A[i+1] = 0

    print(A_sum - sum(A))


main()