import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def main():
    md = 1000000007
    n = II()
    cnt = {}
    cnt[(0, 0)] = [0, 0]
    zero = 0
    for _ in range(n):
        a, b = MI()
        if a * b == 0:
            if a == b == 0:
                zero += 1
            elif a == 0:
                cnt[(0, 0)][0] += 1
            else:
                cnt[(0, 0)][1] += 1
            continue
        par = a * b > 0
        a = abs(a)
        b = abs(b)
        g = gcd(a, b)
        a //= g
        b //= g
        if par:
            cnt.setdefault((a, b), [0, 0])
            cnt[(a, b)][1] += 1
        else:
            cnt.setdefault((b, a), [0, 0])
            cnt[(b, a)][0] += 1
    # print(cnt)
    ans = 1
    for x, y in cnt.values():
        cur = pow(2, x, md) + pow(2, y, md) - 1
        ans = ans * cur % md
    ans += zero
    ans = (ans - 1) % md
    print(ans)

main()
