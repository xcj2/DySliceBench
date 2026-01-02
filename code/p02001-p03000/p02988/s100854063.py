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
    n = II()
    p = LI()

    counter = 0
    for i in range(1,n-1):  # i=2-(n-1)
        if (p[i-1] <= p[i] <= p[i+1]) or (p[i+1] <= p[i] <= p[i-1]):
            counter += 1

    print(counter)


main()