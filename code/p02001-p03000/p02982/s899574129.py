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
    N, D = LI()
    X = []
    for _ in range(N):
        X.append(LI())

    counter = 0
    import itertools
    for i, j in itertools.combinations(range(N),2):
        summation = 0
        for dim in range(D):
            summation += (X[i][dim] - X[j][dim]) **2

        import math
        if math.sqrt(summation).is_integer():
            counter += 1


    print(counter)





main()