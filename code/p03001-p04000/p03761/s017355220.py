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
    oa = ord("a")
    n = II()
    mn = [100000] * 26
    for _ in range(n):
        s = SI()
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - oa] += 1
        for i in range(26):
            if cnt[i] < mn[i]: mn[i] = cnt[i]
    ans = ""
    for i in range(26):
        ans += chr(i + oa) * mn[i]
    print(ans)

main()
