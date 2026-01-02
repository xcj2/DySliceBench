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
    h_list = LI()

    cnt = 0
    max_cnt = 0
    current = h_list[0]
    for h in h_list[1:]:
        if current >= h: # 今が右以上
            cnt += 1
            if cnt >= max_cnt:
                max_cnt = cnt
        else:
            cnt = 0
        current = h
    print(max_cnt)
solve()