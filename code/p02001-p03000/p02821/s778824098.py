import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def ok(c):
        cnt = 0
        i = 0
        for a in aa[::-1]:
            while i < n and a + aa[i] >= c: i += 1
            cnt += i
            if cnt >= m: return True
        return False

    n, m = MI()
    aa = LI()
    aa.sort(reverse=True)
    # 握手の回数がm以上になるような、1回の握手の幸福度の最低値を求める
    l = aa[-1] * 2 - 1
    r = aa[0] * 2 + 1
    while l + 1 < r:
        c = (l + r) // 2
        if ok(c):
            l = c
        else:
            r = c
    min_once = l
    # 幸福度がmin_once以上になる握手の総和を求める
    ans = 0
    i = 0
    s = 0
    cnt = 0
    for a in aa[::-1]:
        while i < n and a + aa[i] >= min_once:
            s += aa[i]
            i += 1
        ans += s + i * a
        cnt += i
    # 握手の回数がmを越えたときはその分の幸福度を引く
    if cnt - m:
        ans -= min_once * (cnt - m)
    print(ans)

main()
