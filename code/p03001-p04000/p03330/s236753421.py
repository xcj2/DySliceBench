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
    N, C = LI()
    D = [[] for _ in range(C)]
    for i in range(C):
        D[i] = LI()
    color = [[] for _ in range(N)]
    for i in range(N):
        color[i] = LI()

    # まず各 mod の色の数を調べる。
    counters = [[0 for _ in range(C+1)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            counters[(i+j)%3][color[i][j]] += 1
    # print(counters)

    sums = [sum(i) for i in counters]

    # 各 mod について、各色を選んだときの違和感を計算する。
    import itertools
    def takemin(variable, val): variable = min(variable, val)
    iwakan = INF
    for selected_cols in itertools.permutations(range(1,C+1), 3):  # 30**3
        sum_ = 0
        for to_, counter  in zip(selected_cols, counters):  # 3
            for from_, num in enumerate(counter):  # 30
                if from_ == 0: continue
                sum_ += D[from_-1][to_-1] * num
        iwakan = min(iwakan, sum_)
    print(iwakan)

main()