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

debug = False

# debug = True
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    N = II()
    divisors = []

    sq = N**0.5
    nearest = -1

    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors.append(i)
            if abs(sq - nearest) > abs(sq-i):
                nearest = i
    dprint(nearest, N//nearest)
    print((nearest-1)+(N//nearest)-1)
solve()