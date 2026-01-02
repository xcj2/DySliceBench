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
    H = LI()

    if N == 1:
        print('Yes')
        return

    for i in range(1, N):
        if H[i-1] < H[i]:
            H[i] -= 1
        elif H[i-1] == H[i]:
            continue
        else:
            print('No')
            break
    else:
        print('Yes')

main()