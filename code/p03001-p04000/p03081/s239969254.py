import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n, q = MI()
    s = SI()
    td = [SI().split() for _ in range(q)]
    ans = n
    # 左に落ちるゴーレムのうち、最右のインデックス
    l = -1
    r = n
    while l + 1 < r:
        m = (l + r) // 2

        def ok(m):
            for t, d in td:
                if s[m] == t: m += (d == "R") * 2 - 1
                if m == -1: return True
                if m == n: return False
            return False

        if ok(m): l = m
        else: r = m
    ans -= l + 1
    # 右に落ちるゴーレムのうち、最左のインデックス
    l = -1
    r = n
    while l + 1 < r:
        m = (l + r) // 2

        def ok(m):
            for t, d in td:
                if s[m] == t: m += (d == "R") * 2 - 1
                if m == -1: return False
                if m == n: return True
            return False

        if ok(m): r = m
        else: l = m
    ans -= n - r

    print(ans)

main()
