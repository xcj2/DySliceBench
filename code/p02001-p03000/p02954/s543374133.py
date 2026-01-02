# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

import re

def solve():
    S = input()

    # print(S)
    # print(re.split("(RL)", S))

    ans = [0 for _ in range(len(S))]
    idx = 0
    rcnt = 0
    lcnt = 0
    pre_rl_idx = -1
    for s in re.split('(RL)', S):
        if s == '':
            continue
        # print(idx, s)



        if s == 'R':
            rcnt += 1
            idx += 1
        elif s == 'L':
            ans[idx - 2] += 1
            idx += 1
        elif s == 'RL':
            ans[idx] += 1
            ans[idx + 1] += 1
            if rcnt > 0:
                r = rcnt // 2
                ans[idx] += r
                ans[idx + 1] += rcnt - r
            pre_rl_idx = idx
            idx += 2
            rcnt = 0
        else:
            for ss in s:
                if ss == 'R':
                    rcnt += 1
                    idx += 1
                elif ss == 'L':
                    lcnt += 1
                    idx += 1

            if lcnt > 0:
                r = lcnt // 2
                ans[pre_rl_idx + 1] += r
                ans[pre_rl_idx] += lcnt - r
                lcnt = 0
        # print(ans)
    # print(ans)
    print(' '.join(list(map(str, ans))))


if __name__ == '__main__':
    solve()
