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
    S = SI()

    ans = int(S)
    for 文字数 in range(1, len(S)):
        for 開始位置 in range(len(S)-文字数+1):
            if 開始位置 == 0 or 開始位置+文字数 == len(S):
                ans += int(S[開始位置:開始位置+文字数]) * 2**(len(S) - 1 - 文字数)
            else:
                ans += int(S[開始位置:開始位置+文字数]) * 2**(len(S) - 1 - 文字数 -1)
    print(ans)

main()