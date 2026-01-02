import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
def main():
    S_ = S()
    S_que = deque(S_)
    Q = I()
    cnt = 0
    for i in range(Q):
        q = LS()
        if int(q[0]) == 1:
            cnt += 1
        elif int(q[0]) == 2:
            if int(q[1]) == 1:
                if cnt % 2 == 0:
                    S_que.appendleft(q[2])
                else:
                    S_que.append(q[2])
            else:
                if cnt % 2 == 1:
                    S_que.appendleft(q[2])
                else:
                    S_que.append(q[2])
    if cnt % 2 == 1:
        S_que.reverse()
    print(''.join(map(str, S_que)))

if __name__ == "__main__":
    main()
