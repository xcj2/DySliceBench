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

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    N = II()
    s_list = []
    for i in range(N):
        s = SI()
        s = sorted(s)
        s_list.append(''.join(s))

    s_list = sorted(s_list)
    dprint(s_list)

    cnt_list = []
    cnt = 0
    current = ''
    for s in s_list:
        if current != s:
            cnt_list.append(cnt+1)
            current = s
            cnt = 0
        else:
            cnt += 1
    cnt_list.append(cnt+1)
    dprint(cnt_list)


    ans = 0
    for cnt in cnt_list:
        ans += cnt*(cnt-1)//2

    print(ans)

solve()