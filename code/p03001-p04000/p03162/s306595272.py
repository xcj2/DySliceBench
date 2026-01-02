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
    happiness = [[] for _ in range(N)]
    for i in range(N):
        happiness[i] = LI()

    result = [[0 for _ in range(3)] for _ in range(N)]
    result[0] = happiness[0]
    for day in range(1,N):  # 10**5   : 夏休みが 10**5 日もある！ 人生は3万日しかない。
        result[day][0] = max(result[day-1][1] + happiness[day][0], result[day-1][2] + happiness[day][0])
        result[day][1] = max(result[day-1][0] + happiness[day][1], result[day-1][2] + happiness[day][1])
        result[day][2] = max(result[day-1][0] + happiness[day][2], result[day-1][1] + happiness[day][2])

    print(max(result[N-1]))

main()