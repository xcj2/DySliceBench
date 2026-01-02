import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def bin_out(aa):
    bb = [format(a, "b") for a in aa]
    print(bb)

def main():
    h, w = MI()
    aa = LLI(h)
    bb = LLI(h)
    max_val=6400
    zero = 1 << max_val
    dp = [0] * w
    dp[0] = zero
    #bin_out(dp)
    for i, (ar, br) in enumerate(zip(aa, bb)):
        for j, (a, b) in enumerate(zip(ar, br)):
            d = abs(a - b)
            if j > 0: dp[j] |= dp[j - 1]
            dp[j] = dp[j] << d | dp[j] >> d
        #bin_out(dp)
    goal = dp[-1]
    for ans in range(max_val + 1):
        if goal & zero << ans or goal & zero >> ans:
            print(ans)
            break

main()
