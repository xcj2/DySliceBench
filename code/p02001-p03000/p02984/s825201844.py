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

    rain = [None]*N
    rain[0] = 0
    for i in range(1,N):
        rain[i] = A[i-1] - rain[i-1]
    looped_ans = A[N-1] - rain[N-1]
    difference = looped_ans//2
    for i in range(N):
        if i%2 == 0:
            rain[i] += difference
        else:
            rain[i] -= difference

    print(' '.join([str(i*2) for i in rain]))


main()