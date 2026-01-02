import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


def judge(bw, lr):
    if bw[0] != "B" or bw[-1] != "B":
        return False

    elif lr.count("L") != lr.count("R"):
        return False

    else:
        return True


def fact(num, mod):
    if num == 1:
        return 1
    else:
        return num * fact(num-1, mod) % mod

n = ni()
bw = lc()
MOD = 10**9 + 7

# 各マスの左端or右端を判定
lr = ['L']
for i in range(2*n-1):
    if bw[i+1] == bw[i]:
        if lr[-1] == "L":
            lr.append("R")
        else:
            lr.append("L")

    else:
        if lr[-1] == "L":
            lr.append("L")
        else:
            lr.append("R")

# 答えが存在するか判定
if judge(bw, lr):
    cnt = 0
    ans = 1
    for lri in lr:
        if lri == "L":
            cnt += 1
        else:
            ans *= cnt
            ans %= MOD
            cnt -= 1

    print(ans * fact(n, MOD) % MOD)
else:
    print(0)