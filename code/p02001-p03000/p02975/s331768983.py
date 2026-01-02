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
    a = LI()

    from collections import Counter

    cnt = Counter(a)

    if len(cnt) == 1 and a[0] == 0:  # all elements are zero
        print('Yes')
        return

    if len(cnt) == 2:
        x, y = cnt.keys()
        if x^y==y and y^y==x and cnt[x]*2==cnt[y]:
            print('Yes')
            return
        if x^x==y and x^y==x and cnt[y]*2==cnt[x]:
            print('Yes')
            return

    if len(cnt) == 3:
        x, y, z = cnt.keys()
        if x^y==z and y^z==x and z^x==y and cnt[x]==cnt[y]==cnt[z]:
            print('Yes')
            return

    print('No')




main()