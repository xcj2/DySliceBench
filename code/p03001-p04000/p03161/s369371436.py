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
    N, K = LI()
    h_li = [0] + LI()
    min_cost_li = [INF for _ in range(N+1)]
    min_cost_li[1] = 0

    for i in range(1,N+1):  # 10**5
        for j in range(1, K+1): # 10**2
            if i+j > N: continue
            min_cost_li[i+j] = min(min_cost_li[i+j], min_cost_li[i] + abs(h_li[i] - h_li[i+j]))

    print(min_cost_li[N])


main()