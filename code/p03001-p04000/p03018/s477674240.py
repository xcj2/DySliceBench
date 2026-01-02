import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    s = SI().replace('BC', 'X')
    cnt = 0
    ans = 0
    for k in s[::-1]:
        if k == 'X':
            cnt += 1
        elif k == 'A':
            ans += cnt
        else:
            cnt = 0
    return ans

print(main())