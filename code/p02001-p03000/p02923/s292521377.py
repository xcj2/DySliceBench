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
    H_li = LI()

    now_count = 0
    max_count = 0
    now_height = H_li[0]

    for h in H_li[1:]:
        if now_height >= h:
            now_count += 1
        else:
            max_count = max(max_count, now_count)
            now_count = 0
        now_height = h
    max_count = max(max_count, now_count)

    print(max_count)

main()