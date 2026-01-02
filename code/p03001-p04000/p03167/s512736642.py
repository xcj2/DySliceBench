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
    H, W = LI()
    maze = [SI() for _ in range(H)]

    ans = [[0 for _ in range(W+1)] for _ in range(H+1)]  # 1つ加えることで番兵とする。Python の場合、[-1] == [N-1] なので、上下左右に加えなくても、右と下に加えるだけでいい（ナナメ移動があるときは注意）。
    ans[0][0] = 1

    for j in range(W):
        for i in range(H):
            if (i, j) == (0, 0): continue
            if maze[i][j] == '#':
                continue
            else:
                ans[i][j] = (ans[i-1][j] + ans[i][j-1])%MOD

    print(ans[H-1][W-1])

main()