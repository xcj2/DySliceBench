import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
from collections import Counter
import bisect
def main():
    N = I()
    A = LI()
    B = LI()
    A_cnt = Counter(A)
    B_cnt = Counter(B)
    for key in B_cnt.keys():
        x = A_cnt[key]
        if B_cnt[key] > N - x:
            print('No')
            exit()
    print('Yes')
    A_m = A_cnt.most_common()
    A_ = []
    for a_m in A_m:
        A_ += [a_m[0]] * a_m[1]
    B_m = deque(B_cnt.most_common())
    ANS = []
    for i in range(N):
        x = B_m[0][0]
        if A_[i] != x:
            ANS.append([A_[i], x])
            B_cnt[x] -= 1
            if B_cnt[x] == 0:
                B_m.popleft()
        elif A_[i] == x:
            if len(B_m) != 1:
                B_m.popleft()
                B_m.append((x, B_cnt[x]))
                y = B_m[0][0]
                ANS.append([x, y])
                B_cnt[y] -= 1
                if B_cnt[y] == 0:
                    B_m.popleft()
            else:
                for ans in ANS:
                    if ans[0] != x and ans[1] != x:
                        ANS.append([x, ans[1]])
                        ans[1] = x
                        break

    ANS.sort(key=lambda tup: tup[0])
    ANS_ = []
    for ans in ANS:
        ANS_.append(ans[1])
    print(' '.join(map(str, ANS_)))

if __name__ == "__main__":
    main()

