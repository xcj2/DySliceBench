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

def main_1(): 
    text = (['Sunny', 'Cloudy'], ['Cloudy', 'Rainy'],['Rainy','Sunny'])
    s = SI()
    for i in text:
        if s == i[0]:
            print(i[1])

def main_2(): 
    s = SI()
    for num, i in enumerate(s):
        if num % 2 == 1: # even
            if not (i in 'LUD'):
                print('No')
                return
        else:
            if not (i in 'RUD'):
                print('No')
                return
    print('Yes')

def main():
    N, K, Q = LI()
    A = [0] * (N+1)
    for _ in range(Q):
        n = II()
        A[n] += 1

    for i in range(N):
        if K - Q + A[i+1] <= 0:
            print('No')
        else:
            print('Yes')

main()