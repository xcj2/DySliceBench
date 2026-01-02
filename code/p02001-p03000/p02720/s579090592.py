import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')
from collections import deque


def solve():
    k = II()
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

    if k <= 9:
        print(q[k-1])
        return

    cnt = len(q)
    while 1:
    # for _ in range(1000000):
        a = q.popleft()
        # print(a)
        one = int(str(a)[-1])
        for i in range(one-1, one+2):
            # print(' ', i)
            if i < 0 or i > 9:
                continue
            num = int(str(a) + str(i))
            cnt += 1
            # print('  ', num, cnt)
            if cnt == k:
                print(num)
                return

            q.append(num)
        # print(q)


if __name__ == '__main__':
    solve()
