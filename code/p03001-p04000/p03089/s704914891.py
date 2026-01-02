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

n = ni()
b = list(li())

num_ofst = [[bi, (i+1) - bi] for i, bi in enumerate(b)]
ans = []

ok = True
while ok and num_ofst:
    cur = -1
    cur_idx = -1
    for i in range(len(num_ofst)-1, -1, -1):
        if num_ofst[i][1] == 0:
            cur = num_ofst[i][0]
            cur_idx = i
            break

        else:
            num_ofst[i][1] -= 1

    if cur != -1:
        num_ofst = num_ofst[:i] + num_ofst[i+1:]
        ans.append(cur)
    else:
        ok = False

if ok:
    print("\n".join(map(str, ans[::-1])))
else:
    print(-1)