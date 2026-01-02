import sys

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MATINT(h): return [list(map(int, input().split())) for _ in range(h)]
def MATSTR(h): return [input() for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
inf = float('inf')
mod = 10 ** 9 + 7

def main():
    N = INT()
    A = LIST()
    M = 0
    b = []
    yaku = [0] * N;
    for i in range(N):
        n = N - i
        if (yaku[n-1] + A[n-1]) % 2:
            b.append(n)
            M += 1
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    yaku[i - 1] += 1
                    if i != n // i:
                        yaku[n//i - 1] += 1
    b.reverse()
    print(M)
    if M != 0:
        print(*b)

if __name__ == '__main__':
    main()
