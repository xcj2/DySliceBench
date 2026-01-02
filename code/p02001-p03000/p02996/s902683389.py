import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N = II()
    AB = []
    for _ in range(N):
        a, b = LI()
        AB.append([b, a])
    AB.sort()
    ans = True
    time = 0
    for b, a in AB:
        time += a
        if time > b:
            ans = False
            break
    ans = YesNo(ans)
    return ans

print(main())