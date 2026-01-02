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

def even_digits(i):
    if (1 <= i <= 9) or (100 <= i <= 999) or (10000 <= i <= 99999) or (1000000 <= i <= 9999999):
        return True
    else: return False

def main(): 
    N = II()
    counter = 0
    for i in range(1, N+1):
        if even_digits(i):
            counter+=1
    print(counter)

main()