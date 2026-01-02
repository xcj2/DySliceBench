import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def LILI(n): return [LI() for _ in range(n)]
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N, K = LI()
    S = SI()

    wakareme = []
    current_koufuku = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            wakareme.append(i)
        else:
            current_koufuku += 1

    if 2*K < len(wakareme):
        print(current_koufuku + 2 * K)  # K 回の操作すべてで幸福を+2できる。
        return
    else:
        print(N-1)  # 末端以外の人すべてを幸福にできる。
        return


main()